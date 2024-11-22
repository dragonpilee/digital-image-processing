import numpy as np
import cv2

img_src = cv2.imread('lena.jpg')
kernel = np.array([[0.0, -1.0, 0.0],
                   [-1.0, 4.0, -1.0],
                   [0.0, -1.0, 0.0]])
kernel = kernel / (np.sum(kernel) if np.sum(kernel) != 0 else 1)
img_rst = cv2.filter2D(img_src, -1, kernel)
cv2.imshow('result.jpg', img_rst)
cv2.waitKey(0)
