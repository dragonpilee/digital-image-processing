import numpy as np
import matplotlib.pyplot as plt
import PIL
import cmath

def DFT2D(image):
    data = np.asarray(image)
    if len(data.shape) == 3:  # Check if the image is color
        data = np.mean(data, axis=-1)  # Convert color image to grayscale
    
    M, N = data.shape
    dft2d = np.zeros((M, N), dtype=complex)
    
    for k in range(M):
        for l in range(N):
            sum_matrix = complex(0)
            for m in range(M):
                for n in range(N):
                    e = cmath.exp(-2j * np.pi * ((k * m) / M + (l * n) / N))
                    sum_matrix += data[m, n] * e
            dft2d[k, l] = sum_matrix
    
    return dft2d

# Load and resize the image
img = PIL.Image.open("vis.jpg")
img2 = img.resize((50, 50))

# Compute the DFT
dft = DFT2D(img2)

# Plot the original image and the magnitude of its DFT
plt.subplot(121), plt.imshow(img2, cmap='gray')
plt.title('IMAGE'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(np.abs(dft), cmap='gray')  # Plotting the magnitude of the DFT
plt.title('2DDFT Magnitude'), plt.xticks([]), plt.yticks([])
plt.show()

