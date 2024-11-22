import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')
hist1 = cv2.calcHist([img],[0],None,[256],[0,256])
hist2 = cv2.calcHist([img],[1],None,[256],[0,256])
hist3 = cv2.calcHist([img],[2],None,[256],[0,256])

plt.subplot(221), plt.imshow(img)
plt.subplot(222), plt.plot(hist1), plt.plot(hist2), plt.plot(hist3)
plt.xlim([0,256])
plt.show()
