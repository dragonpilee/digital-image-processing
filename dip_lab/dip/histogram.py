import cv2
from matplotlib import pyplot as plt

img = cv2.imread('vis.jpg', 0)
histr = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.plot(histr, color='black')
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()

