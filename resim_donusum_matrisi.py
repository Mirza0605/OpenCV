import cv2
import numpy as np

img = cv2.imread("C:/Users/Master/Desktop/OpenCV/resim_donusum_matrisi/7.jpg", 0)
row,col = img.shape

M = np.float32([[1,0,10], [0, 1, 70]]) # pencere ile resim arasındaki boşluğu ayarlar.
dst = cv2.warpAffine(img, M, (col,row))

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()