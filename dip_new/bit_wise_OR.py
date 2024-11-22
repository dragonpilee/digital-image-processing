import cv2
import numpy as np

# Read images
img1 = cv2.imread('apple.jpg')
img2 = cv2.imread('baboon.jpg')

# Resize img2 to match the dimensions of img1
img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Perform bitwise OR operation
dest_or = cv2.bitwise_or(img1, img2_resized, mask=None)

# Display the result
cv2.imshow('Bitwise OR', dest_or)
cv2.waitKey(0)
cv2.destroyAllWindows()
