import cv2
import numpy as np

img = cv2.imread('stuff.jpg')
img_log = (np.log(img+1)/(np.log(1+np.max(img))))*255
img_log = np.array(img_log, dtype=np.uint8)

cv2.imshow('log_image', img_log)
cv2.imshow('original_img', img)
cv2.waitKey(0)
