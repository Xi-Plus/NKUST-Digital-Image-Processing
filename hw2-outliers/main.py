import argparse

import cv2
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument('image', nargs='?', default='twins_sp.png')
parser.add_argument('-d', type=float, default=0.2)

args = parser.parse_args()
print(args)

img = cv2.imread(args.image, cv2.IMREAD_UNCHANGED)
print('shape', img.shape)
height = img.shape[0]
width = img.shape[1]
imagesize = height * width

new_img = img.copy()
for h in range(1, height - 1):
    for w in range(1, width - 1):
        avg = 0
        for dh in range(-1, 2):
            for dw in range(-1, 2):
                if dh == 0 and dw == 0:
                    continue
                avg += int(img[h + dh, w + dw])
        avg /= 8
        if abs(img[h, w] - avg) > 255 * args.d:
            new_img[h, w] = avg

figure = plt.figure()

figure.add_subplot(1, 2, 1)
plt.imshow(img, cmap='gray')

figure.add_subplot(1, 2, 2)
plt.imshow(new_img, cmap='gray')

plt.show(block=True)
