import cv2
import numpy as np

img = cv2.imread('flower.png')

flag = ''.join([bin(ord(x))[2:].zfill(8) for x in list(input("input flag: "))])
flag += '0' * (img.shape[0] * img.shape[1] * img.shape[2] - len(flag))

print(flag)
print(len(flag))

enc_img = []

cnt = 0

for i in img:
    img_line = []
    for j in i:
        # [r, g, b]と書いてますが本当は[b, g, r]でした。m(__)m
        r, g, b = [[y for y in list(bin(x)[2:])] for x in j]
        r[-1] = flag[cnt]
        g[-1] = flag[cnt + 1]
        b[-1] = flag[cnt + 2]
        cnt += 3
        img_line.append([int(x, 2) for x in [''.join(r), ''.join(g), ''.join(b)]])
    enc_img.append(img_line)
cv2.imwrite('enc_flower.png', np.array(enc_img))
