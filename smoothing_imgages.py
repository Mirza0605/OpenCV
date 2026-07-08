import cv2
import numpy as np

img_filter = cv2.imread("C:/Users/Master/Desktop/OpenCV/smoothing_images/3.png")
img_median = cv2.imread("C:/Users/Master/Desktop/OpenCV/smoothing_images/2.png")
img_bilateral = cv2.imread("C:/Users/Master/Desktop/OpenCV/smoothing_images/4.png")

blur =cv2.blur(img_filter,(11,11)) # sadece pozitif tek sayılar olmalı. blur yumuşatır.

# blur_g = cv2.GaussianBlur(img_filter, (5,5), cv2.BORDER_DEFAULT)

# cv2.imshow("original",img_filter)
# cv2.imshow("blur",blur)
# cv2.imshow("blur2",blurg)

# blur_m = cv2.medianBlur(img_median, 9)
# cv2.imshow("original", img_median)
# cv2.imshow("blur_m", blur_m)

blur_b = cv2.bilateralFilter(img_bilateral, 9, 75, 75)
cv2.imshow("original", img_bilateral)
cv2.imshow("blur_b", blur_b)

cv2.waitKey(0)
cv2.destroyAllWindows()