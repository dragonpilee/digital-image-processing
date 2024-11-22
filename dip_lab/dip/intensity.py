import cv2
import numpy as np
import matplotlib.pyplot as plt

img_bgr = cv2.imread('vis.jpg', 1)

# Negate the original image
img_neg = 1 - img_bgr

# Apply log transform
c = 255 / (np.log(1 + np.max(img_bgr)))
log_transformed = c * np.log(1 + img_bgr)
log_transformed = np.array(log_transformed, dtype=np.uint8)

# Trying 4 gamma values
for gamma in [0.1, 0.5, 1.2, 2.2]:
    # Apply gamma correction
    gamma_corrected = np.array(255 * (img_bgr / 255) ** gamma, dtype='uint8')

    # Function to map each intensity level to output intensity level
    def pixelVal(pix, r1, s1, r2, s2):
        if 0 <= pix <= r1:
            return (s1 / r1) * pix
        elif r1 < pix <= r2:
            return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
        else:
            return pix

    # Define parameters
    r1 = 70
    s1 = 0
    r2 = 140
    s2 = 255

    pixelVal_vec = np.vectorize(pixelVal)

    # Apply contrast stretching
    contrast_stretched = pixelVal_vec(img_bgr, r1, s1, r2, s2)

    plt.subplot(3, 3, 1), plt.imshow(img_bgr)
    plt.title('ORIGINAL IMAGE'), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, 2), plt.imshow(img_neg)
    plt.title('NEGATIVE IMAGE'), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, 3), plt.imshow(log_transformed)
    plt.title('LOG TRANSFORMED'), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, 4), plt.imshow(gamma_corrected)
    plt.title(f'GAMMA {gamma}'), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, 5), plt.imshow(gamma_corrected)
    plt.title(f'GAMMA {gamma}'), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, 6), plt.imshow(gamma_corrected)
    plt.title(f'GAMMA {gamma}'), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, 7), plt.imshow(gamma_corrected)
    plt.title(f'GAMMA {gamma}'), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, 8), plt.imshow(contrast_stretched)
    plt.title('CONTRAST STRETCHED'), plt.xticks([]), plt.yticks([])

    plt.show()

