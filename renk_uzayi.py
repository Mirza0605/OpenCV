import cv2

img = cv2.imread("C:/Users/Master/Desktop/OpenCV/temel_islemler/klon.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # rgbye dönüştürdü
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # hsvye dönüştürdü
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # griye dönüştürdü


cv2.imshow("Klon", img)
cv2.imshow("Klon RGB", img_rgb)
cv2.imshow("Klon HSV", img_hsv)
cv2.imshow("Klon GRAY", img_gray)


cv2.waitKey(0)
cv2.destroyAllWindows()