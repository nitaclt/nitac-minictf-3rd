import gmpy2

c = int(input("ciphertext: "))
r = int(input("r: "))
q = int(input("q: "))
n = int(input("len(b): "))

s = gmpy2.invert(r, q)
msg = c * s % q
res = ''
for i in range(n - 1, -1, -1):
    if msg >= p[i]:
        res = '1' + res
        msg -= p[i]
    else:
        res = '0' + res
print(res)