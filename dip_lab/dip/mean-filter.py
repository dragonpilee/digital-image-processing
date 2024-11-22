import numpy as np
import cv2
from matplotlib import pyplot as plt

def apply_mean_filter(image, figure_size):
    return cv2.blur(image, (figure_size, figure_size))

def plot_images(original, processed, title_original, title_processed):
    plt.figure(figsize=(11, 6))

    plt.subplot(121)
    plt.imshow(original)
    plt.title(title_original)
    plt.xticks([]), plt.yticks([])

    plt.subplot(122)
    plt.imshow(processed)
    plt.title(title_processed)
    plt.xticks([]), plt.yticks([])

    plt.show()

if __name__ == "__main__":
    # Load the image
    image = cv2.imread('vis.jpg')

    # Check if the image is loaded successfully
    if image is None:
        print("Error: Could not open or read the image.")
    else:
        # Apply mean filter
        figure_size = 9
        new_image = apply_mean_filter(image, figure_size)

        # Display images
        plot_images(image, new_image, 'Original', 'Mean Filter')

