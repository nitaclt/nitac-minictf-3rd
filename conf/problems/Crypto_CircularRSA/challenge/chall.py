from Crypto.Util.number import getPrime
from secret import flag

m = int.from_bytes(flag, byteorder='big')
assert m.bit_length() < 1024

p, q = getPrime(512), getPrime(512)
n = p * q
e = 0x10001
c = pow(m, e, n)
rr = (p**2 + q**2) % n

print("(p, q) is over R: x^2 + y^2 = {} mod {}".format(rr, n))
print("c = {}".format(c))
