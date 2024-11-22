import cv2

# Read the images
img1 = cv2.imread('apple.jpg')
img2 = cv2.imread('baboon.jpg')

# Resize img2 to match the dimensions of img1
img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Subtract the images
result_image = cv2.subtract(img1, img2_resized)

# Display the subtracted image
cv2.imshow('Subtracted Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
