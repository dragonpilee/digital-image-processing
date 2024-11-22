import cv2

# Read the images
ap = cv2.imread('apple.jpg')
hf = cv2.imread('baboon.jpg')

# Resize images to the same size if needed
ap = cv2.resize(ap, (hf.shape[1], hf.shape[0]))

# Define the alpha blending factor
alpha = 0.5

# Perform alpha blending
blended_img = cv2.addWeighted(ap, alpha, hf, 1 - alpha, 0)

# Display the blended image
cv2.imshow('Blended Image', blended_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
