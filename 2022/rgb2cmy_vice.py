import cv2
import numpy as np

# Read the RGB image
rgb_image = cv2.imread('pool.jpg')

# Convert the RGB image to CMY image
cmy_image = 255 - rgb_image

# Save the CMY image
cv2.imwrite('cmy_image.jpg', cmy_image)

# Display the CMY image
cv2.imshow('CMY Image', cmy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Read the CMY image
cmy_image = cv2.imread('cmy_image.jpg')

if cmy_image is not None:
    # Convert the CMY image to RGB image
    rgb_image = 255 - cmy_image

    # Display the RGB image
    cv2.imshow('RGB Image', rgb_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Unable to read the CMY image file.")
