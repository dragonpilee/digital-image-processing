import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('vis.jpg')

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

plt.subplot(2, 3, 1), plt.imshow(thresh1, cmap='gray')
plt.title('BINARY'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 2), plt.imshow(thresh2, cmap='gray')
plt.title('BINARY INVERTED'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 3), plt.imshow(thresh3, cmap='gray')
plt.title('TRUNCATED'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 4), plt.imshow(thresh4, cmap='gray')
plt.title('SET TO 0'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5), plt.imshow(thresh5, cmap='gray')
plt.title('SET TO 0 INVERTED'), plt.xticks([]), plt.yticks([])

plt.show()

