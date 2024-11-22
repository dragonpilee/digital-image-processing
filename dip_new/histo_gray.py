import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image in grayscale mode
img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate the histogram of the image
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Plot the histogram using matplotlib
plt.hist(img.ravel(), 256, [0, 256])
plt.title('Histogram for grayscale image')
plt.show()

# Display the image in a window titled 'Cat'
cv2.imshow('Cat', img)

# Wait for a key press to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
