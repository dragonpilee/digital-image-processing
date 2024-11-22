import cv2
import numpy as np
from matplotlib import pyplot as plt

def apply_filter(image_fft, filter_kernel):
    """
    Apply filter in frequency domain.
    """
    filtered_image_fft = image_fft * filter_kernel
    return filtered_image_fft

# Read the image
image = cv2.imread('pool.jpg', 0)

# Compute the 2-D DFT
image_fft = np.fft.fft2(image)
image_fft_shifted = np.fft.fftshift(image_fft)

# Define a low-pass filter kernel (Gaussian filter)
rows, cols = image.shape
crow, ccol = rows // 2 , cols // 2
d = 30  # cutoff frequency
filter_kernel = np.zeros((rows, cols), np.uint8)
for i in range(rows):
    for j in range(cols):
        if np.sqrt((i - crow)**2 + (j - ccol)**2) <= d:
            filter_kernel[i, j] = 1

# Apply the filter in frequency domain
filtered_image_fft_shifted = apply_filter(image_fft_shifted, filter_kernel)

# Inverse FFT to obtain the filtered image
filtered_image_fft = np.fft.ifftshift(filtered_image_fft_shifted)
filtered_image = np.fft.ifft2(filtered_image_fft)
filtered_image = np.abs(filtered_image)

# Plot the original and filtered images
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()
