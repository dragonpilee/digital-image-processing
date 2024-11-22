import cv2

img = cv2.imread('lena.jpg')
h, w, c = img.shape
print('width:', w)
print('height:', h)
print('channel:', c)
