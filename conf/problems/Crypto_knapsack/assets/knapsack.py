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

# 平文
a = list(input("flag: "))
a = ''.join([bin(ord(x))[2:].zfill(8) for x in a])
a = np.array([int(x) for x in list(a)])

# 超増加数列
p = superIncreaseSequence(len(a))
w = np.array(p)

# 超増加数列の総和を超える数
q = random.randint(w[-1], 2 * w[-1])
while True:
    r = random.randint(1, q)
    if gmpy2.gcd(r, q) == 1:
        break

# 公開鍵の作成
b = np.array([(r * i % q) for i in w])

# 暗号文
c = sum(a * b)

print("ciphertext: ", c)
print("r:", r)
print("q:", q)
print("publickey:", b.tolist())

with open("ciphertext.txt", "w") as f:
    f.write(str(c))
with open("publickey.txt", "w") as f:
    f.write(', '.join([str(x) for x in b.tolist()]))
with open("w.txt", "w") as f:
    f.write(', '.join([str(x) for x in p]))
with open("r.txt", "w") as f:
    f.write(str(r))
with open("q.txt", "w") as f:
    f.write(str(q))

# 密度の計算
print(max(b))
density = len(b) / np.log2(float(max(b)))
print("density:", density)

with open("density.txt", "w") as f:
    f.writelines(str(density))

# solve
s = gmpy2.invert(r, q)
msg = c * s % q
res = ''
for i in range(len(b) - 1, -1, -1):
    if msg >= p[i]:
        res = '1' + res
        msg -= p[i]
    else:
        res = '0' + res
print(res)

plain = []
cnt = 1
ch = ""
for i in list(res):
    ch += i
    if cnt % 8 == 0:
        plain.append(ch)
        ch = ""
    cnt += 1

plain = [chr(int(x, 2)) for x in plain]
print(''.join(plain))