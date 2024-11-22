import cv2
import numpy as np

# Read the image in grayscale
image = cv2.imread('pool.jpg', cv2.IMREAD_GRAYSCALE)

# Apply thresholding
threshold_value = 127
max_value = 255
ret, thresholded_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)

# Display the original and thresholded images
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
