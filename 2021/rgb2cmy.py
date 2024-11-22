import cv2
import numpy as np

def rgb_to_cmy(rgb_image):
    """
    Convert an RGB image into a CMY image.

    Parameters:
    rgb_image (numpy.ndarray): The input RGB image.

    Returns:
    numpy.ndarray: The CMY image.
    """
    cmy_image = 1 - rgb_image / 255.0
    return cmy_image

if __name__ == "__main__":
    # Read the RGB image
    image_path = input("Enter the path to the RGB image: ")
    rgb_image = cv2.imread(image_path)

    if rgb_image is None:
        print("Error: Unable to read the image.")
    else:
        # Convert RGB image to CMY image
        cmy_image = rgb_to_cmy(rgb_image)

        # Display the CMY image
        cv2.imshow('CMY Image', cmy_image)
        cv2.waitKey(0)
