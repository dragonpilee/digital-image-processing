import cv2
import numpy as np

# Read images
img1 = cv2.imread('apple.jpg')
img2 = cv2.imread('baboon.jpg')

# Resize images to match dimensions
img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Perform bitwise AND operation
dest_and = cv2.bitwise_and(img1, img2_resized, mask=None)

# Display the result
cv2.imshow('Bitwise And', dest_and)
cv2.waitKey(0)
cv2.destroyAllWindows()
