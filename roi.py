# roi ---> region of interest ---> ilgi alanı
import cv2

img = cv2.imread("C:/Users/Master/Desktop/OpenCV/temel_islemler/klon.jpg")
# print(img.shape[:2]) #resmin boyutunu verir.

roi = img[15:110, 100:250] # resmin içinden bir parça almamızı sağlar.

cv2.imshow("Klon", img)
cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()