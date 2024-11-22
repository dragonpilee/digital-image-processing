import cv2
img = cv2.imread('pool.jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
filteredImg = cv2.medianBlur(grayImg, ksize=5)
cv2.imshow('Original image', grayImg)
cv2.imshow('Filtered image', filteredImg)
cv2.waitKey(0)
cv2.destroyAllWindows()