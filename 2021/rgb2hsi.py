import cv2
import numpy as np

def rgb_to_hsi(rgb_image):
    """
    Convert an RGB image into an HSI image.

    Parameters:
    rgb_image (numpy.ndarray): The input RGB image.

    Returns:
    numpy.ndarray: The HSI image.
    """
    # Normalize the pixel values to the range [0, 1]
    rgb_image = rgb_image.astype(np.float32) / 255.0

    # Separate the color channels
    red, green, blue = rgb_image[:, :, 0], rgb_image[:, :, 1], rgb_image[:, :, 2]

    # Compute Intensity
    intensity = (red + green + blue) / 3.0

    # Compute Saturation
    min_rgb = np.minimum(np.minimum(red, green), blue)
    saturation = 1 - 3 * min_rgb / (red + green + blue + 1e-6)

    # Compute Hue
    theta = np.arccos((0.5 * ((red - green) + (red - blue))) /
                      ((np.sqrt((red - green) ** 2 + (red - blue) * (green - blue))) + 1e-6))
    hue = theta.copy()
    hue[blue > green] = 2 * np.pi - hue[blue > green]
    hue = hue / (2 * np.pi)

    # Stack the HSI channels back together
    hsi_image = np.stack((hue, saturation, intensity), axis=-1)

    return hsi_image

if __name__ == "__main__":
    # Read the RGB image
    image_path = input("Enter the path to the RGB image: ")
    rgb_image = cv2.imread(image_path)

    if rgb_image is None:
        print("Error: Unable to read the image.")
    else:
        # Convert RGB image to HSI image
        hsi_image = rgb_to_hsi(rgb_image)

        # Display the HSI image
        cv2.imshow('HSI Image', hsi_image)
        cv2.waitKey(0)
