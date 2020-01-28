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