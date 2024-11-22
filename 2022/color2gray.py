import cv2

# Read the color image
color_image = cv2.imread('pool.jpg')

# Convert the color image to grayscale
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Display the original color image and the grayscale image
cv2.imshow('Color Image', color_image)
cv2.imshow('Grayscale Image', gray_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
