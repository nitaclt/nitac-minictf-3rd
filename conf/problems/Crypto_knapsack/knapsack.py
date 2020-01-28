import numpy as np
import gmpy2
import random

def superIncreaseSequence(n):
    sequence = [1]
    tmp = 1
    for i in range(1, n):
        sequence.append(random.randint(tmp + 1, 3 * tmp))
        tmp += sequence[i]
    print("superIncreaceSequence:", sequence)
    return sequence

a = list(input("flag: "))
a = ''.join([bin(ord(x))[2:].zfill(8) for x in a])
a = np.array([int(x) for x in list(a)])

p = superIncreaseSequence(len(a))
w = np.array(p)

q = random.randint(w[-1], 2 * w[-1])
while True:
    r = random.randint(1, q)
    if gmpy2.gcd(r, q) == 1:
        break

b = np.array([(r * i % q) for i in w])

c = sum(a * b)

with open("ciphertext.txt", "w") as f:
    f.write(str(c))
with open("publickey.txt", "w") as f:
    f.write(', '.join([str(x) for x in b.tolist()]))