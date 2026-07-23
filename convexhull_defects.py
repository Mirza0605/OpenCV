import cv2
import numpy as np

img = cv2.imread("C:/Users/Master/Desktop/OpenCV/convexhull_defects/star.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = cv2.convexHull(contours[0], returnPoints=False)

defects = cv2.convexityDefects(contours[0], hull)

if defects is not None:
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i]
        start = tuple(contours[0][s][0])
        end = tuple(contours[0][e][0])
        far = tuple(contours[0][f][0])

        cv2.line(img, start, end, [0, 255, 0], 2)
        cv2.circle(img, far, 5, [0, 0, 255], -1)

cv2.imshow("Convex Hull Defects", img)
cv2.waitKey(0)
cv2.destroyAllWindows()