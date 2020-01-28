import cv2

img = cv2.imread('../enc_flower.png')

flag = []

for i in img:
    for j in i:
        r, g, b = [bin(x) for x in j]
        flag.append(r[-1])
        flag.append(g[-1])
        flag.append(b[-1])


print(''.join(flag))