import argparse

import cv2
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument('image', nargs='?', default='coins.tif')

args = parser.parse_args()
print(args)

img = cv2.imread(args.image, cv2.IMREAD_UNCHANGED)
print('shape', img.shape)
height = img.shape[0]
width = img.shape[1]
imagesize = height * width

count = {}
for i in range(256):
    count[i] = 0

for v in img.ravel():
    count[v] += 1

# threshold

all_pixel_sum = 0
for i in range(256):
    all_pixel_sum += i * count[i]

pixel_sum = 0
count_back = 0
max_var = 0
threshold1 = 0
threshold2 = 0

for i in range(256):
    count_back += count[i]
    if count_back == 0:
        continue
    count_front = imagesize - count_back
    if count_front == 0:
        break
    pixel_sum += i * count[i]
    avg_back = pixel_sum / count_back
    avg_front = (all_pixel_sum - pixel_sum) / count_front
    var = count_back * count_front * (avg_back - avg_front) * (avg_back - avg_front)
    if var >= max_var:
        threshold1 = i
        if var > max_var:
            threshold2 = i
        max_var = var

threshold = (threshold1 + threshold2) // 2
print('threshold', threshold)
new_img = img.copy()
new_img[new_img < threshold] = 0
new_img[new_img >= threshold] = 255

figure = plt.figure()

figure.add_subplot(1, 2, 1)
plt.imshow(img, cmap='gray')

figure.add_subplot(1, 2, 2)
plt.imshow(new_img, cmap='gray')

plt.show(block=True)
