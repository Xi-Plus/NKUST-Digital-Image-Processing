import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('pout.tif', cv2.IMREAD_UNCHANGED)
print('shape', img.shape)
height = img.shape[0]
width = img.shape[1]

figure = plt.figure()

figure.add_subplot(1, 2, 1)
plt.imshow(img, cmap='gray')

figure.add_subplot(1, 2, 2)
plt.hist(img.ravel(), bins=255, range=(0, 255))
plt.ylabel('count')

plt.show(block=True)

count = {}
for v in img.ravel():
    if v not in count:
        count[v] = 0
    count[v] += 1
values = []
cdf = []

for v in sorted(count.keys()):
    values.append(v)
    cdf.append(count[v])
print(cdf)
for i in range(len(cdf) - 1):
    cdf[i + 1] += cdf[i]
print(cdf)

newvaluetable = {}
for i in range(len(values)):
    newvaluetable[values[i]] = round(
        (cdf[i] - cdf[0]) / (height * width - cdf[0]) * 255)

print(newvaluetable)

newimg = np.empty((height, width), dtype=np.uint8)
for h in range(height):
    for w in range(width):
        newimg[h, w] = newvaluetable[img[h, w]]

figure = plt.figure()

figure.add_subplot(1, 2, 1)
plt.imshow(newimg, cmap='gray')

figure.add_subplot(1, 2, 2)
plt.hist(newimg.ravel(), bins=255, range=(0, 255))
plt.ylabel('count')

plt.show(block=True)
