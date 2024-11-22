import cv2

img = cv2.imread("lena.jpg", 0)
img = -img
print(img)
cv2.imshow("name", img)
cv2.waitKey(0)
cv2.imwrite("lena.jpg", img)
