import numpy as np
import cv2

img = cv2.imread('sq.jpg')
gamma_two_point_two = np.array(255*(img/255)**2.2, dtype='uint8')
gamma_point_four = np.array(255*(img/255)**0.4, dtype='uint8')
img3 = cv2.hconcat([gamma_two_point_two, gamma_point_four])
cv2.imshow('a2', img3)
cv2.waitKey(0)