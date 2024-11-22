import numpy as np
import cv2

img = cv2.imread('lena.jpg', 1)
row, col, ch = img.shape
p = 0.5
a = 0.009

# Make a copy of the original image
noisy = img.copy()

# Salt mode
num_salt = np.ceil(a * img.size * p)
coords = [np.random.randint(0, i - 1, int(num_salt)) for i in img.shape]
noisy[tuple(coords)] = 255

# Pepper mode
num_pepper = np.ceil(a * img.size * (1. - p))
coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in img.shape]
noisy[tuple(coords)] = 0

cv2.imshow('noisy', noisy)
median_blur = cv2.medianBlur(noisy, 3)
cv2.imshow('median_blur', median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
