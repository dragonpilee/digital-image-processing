import cv2
import numpy as np

img = cv2.imread("lena.jpg")
img_neg = 255 - img
cv2.imshow("negative", img_neg)
cv2.waitKey(0)
