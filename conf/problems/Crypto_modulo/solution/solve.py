from ptrlib import *
from Crypto.Util.number import isPrime

th = 1 << 256

w = 1
pairs = []
for n in range(123455, 0, -1):
    if not isPrime(n):
        continue
    
    sock = Socket("0.0.0.0", 7001)
    sock.sendline(str(n))
    sock.recvuntil(": ")
    pairs.append((int(sock.recvline()), n))
    print(pairs[-1])
    sock.close()

    w *= n
    if w > th:
        break

f = chinese_remainder_theorem(pairs)
print(int.to_bytes(f[0], length=256//8, byteorder='big'))
