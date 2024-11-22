import cv2
import numpy as np

def edge_detection_sobel(image):
    """
    Perform edge detection using the Sobel operator.
    """
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (3, 3), 0)

    # Calculate gradients using the Sobel operator
    gradient_x = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3)

    # Compute the magnitude of the gradients
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
    gradient_magnitude *= 255.0 / gradient_magnitude.max()

    # Convert gradient magnitude to uint8
    gradient_magnitude = np.uint8(gradient_magnitude)

    return gradient_magnitude

# Read the image
image = cv2.imread('pool.jpg')

# Perform edge detection using the Sobel operator
edges = edge_detection_sobel(image)

# Display the original and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detected (Sobel)', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
