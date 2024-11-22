import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the grayscale image
image = cv2.imread('pool.jpg', cv2.IMREAD_GRAYSCALE)

# Negative Identity Transformation
negative_image = 255 - image

# Log Transformation
c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))

# Power-law Transformation (Gamma correction)
gamma = 0.5
power_law_image = np.power(image, gamma)

# Display the original and transformed images
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(negative_image, cmap='gray')
plt.title('Negative Identity Transformation')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(log_image, cmap='gray')
plt.title('Log Transformation')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(power_law_image, cmap='gray')
plt.title('Power-law Transformation (Gamma 0.5)')
plt.axis('off')

plt.tight_layout()
plt.show()
