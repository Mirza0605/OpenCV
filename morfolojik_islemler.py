import cv2
import numpy as np

img = cv2.imread("C:/Users/Master/Desktop/OpenCV/7.jpg",0)

# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.erode(img,kernel,iterations= 1)
# cv2.imshow("img",img)
# cv2.imshow("erosion",erosion)       ## siyahlıklar artar.

# kernel = np.ones((5,5),np.uint8)
# dilation = cv2.dilate(img,kernel,iterations= 5)
# cv2.imshow("img",img)
# cv2.imshow("dilaiton",dilation) ## beyazlıklar artar.

# kernel = np.ones((5,5),np.uint8)
# opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
# cv2.imshow("img",img)
# cv2.imshow("opening",opening)  ## gürültü siler.

# kernel = np.ones((5,5),np.uint8)
# closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
# cv2.imshow("img",img)
# cv2.imshow("closing",closing) ## şeklin içindeki uyumsuzukları giderir.


# kernel = np.ones((5,5),np.uint8)
# gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
# cv2.imshow("img",img)
# cv2.imshow("gradient",gradient) ## resmin uç kısımlarını kearlarını beyaz yapar kalan yerler siyah

kernel = np.ones((5,5),np.uint8)
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
cv2.imshow("img",img)
cv2.imshow("tophat",tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()