import cv2
import numpy as np

# Read the images
img1 = cv2.imread('apple.jpg')
img2 = cv2.imread('baboon.jpg')

# Resize the images to have the same dimensions
img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

# Perform the bitwise XOR operation
dest_xor = cv2.bitwise_xor(img1, img2)

# Display the result
cv2.imshow('Bitwise XOR', dest_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()
