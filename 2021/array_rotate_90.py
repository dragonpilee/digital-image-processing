from PIL import Image
import numpy as np

def rotate_90(image_array):
    # Perform a 90-degree rotation on the image array
    rotated_array = np.rot90(image_array)
    return rotated_array

if __name__ == "__main__":
    # Input the grayscale image file
    image_path = input("Enter the path to the grayscale image: ")

    # Open the image file
    image = Image.open(image_path)

    # Convert the image to grayscale if it's not already in grayscale
    image = image.convert("L")

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Perform a 90-degree rotation on the image
    rotated_image_array = rotate_90(image_array)

    # Display or save the rotated image
    rotated_image = Image.fromarray(rotated_image_array)

    # Save the rotated image to a file or display it
    rotated_image.show()
