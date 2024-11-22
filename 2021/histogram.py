import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_histogram(image):
    """
    Display the histogram of a color image.

    Parameters:
    image (numpy.ndarray): The color image.
    """
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the histogram
    histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    # Display the histogram
    plt.figure()
    plt.title('Grayscale Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.plot(histogram, color='black')
    plt.xlim([0, 256])
    plt.show()

if __name__ == "__main__":
    # Read the color image
    image_path = input("Enter the path to the color image: ")
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Unable to read the image.")
    else:
        # Display the color image
        cv2.imshow('Color Image', image)
        cv2.waitKey(0)
        
        # Display the histogram
        display_histogram(image)

