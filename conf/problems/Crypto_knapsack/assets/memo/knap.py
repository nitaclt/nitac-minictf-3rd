import numpy as np
import sys
import gmpy2
import random

def superIncreaseSequence(n):
    sequence = [1]
    tmp = 1
    for i in range(1, n):
        sequence.append(random.randint(tmp + 1, 2 * tmp))
        tmp += sequence[i]
    print("superIncreaceSequence:", sequence)
    return sequence



# 平文
a = list(input("flag: "))
# a = list("NITAC{This_is_flag}")
# a = bin(int(a.encode().hex(), 16))[2:]
a = ''.join([bin(ord(x))[2:].zfill(8) for x in a])
print(a)
a = np.array([int(x) for x in list(a)])
print('a:', a)
print('len(a):', len(a))
# 超増加数列
p = superIncreaseSequence(len(a))
w = np.array(p)
print('sun(w):', sum(w))
# 超増加数列の総和を超える数
# q = 4444120783
q = random.randint(w[-1], 2 * w[-1])
while True:
    r = random.randint(1, q)
    if gmpy2.gcd(r, q) == 1:
        break

# 公開鍵の作成
b = np.array([(r * i % q) for i in w])
print(len(a), len(b))
print("pub:\n", b.tolist())

# 暗号文
c = sum(a * b)
print("enc:", c)

'''
# ここまで暗号化
publickey=b secretkey=(w,q,r)
# ここから復号化
'''

s = gmpy2.invert(r, q)
msg = c * s % q
res = ''
n = len(p)
for i in range(n - 1, -1, -1):
    if msg >= p[i]:
        res = '1' + res
        msg -= p[i]
    else:
        res = '0' + res
print(res)
print(q)
print(r)
print(c)
'''
# mrは整数の合同におけるrの逆元
mr = 0
for i in range(1145141919810931893):
    if (r * i) % q == 1:
        mr = i
        break

# wの部分和になるはず
m = (c * mr) % q

# 平文を求める
ans = []
for i in w[::-1]:
    # print(i, m)
    if m >= i:
        ans.append(1)
        m -= i
    else:
        ans.append(0)
print(ans[::-1])
'''