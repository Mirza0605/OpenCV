import cv2

img = cv2.imread("C:/Users/Master/Desktop/klon.jpg",0) # resmi okur. 0 ise resmi gri tonlar
# print(img) => matris olarak çıktı verir.

cv2.namedWindow("Image",cv2.WINDOW_NORMAL) # pencereyi büyütüp küçültmemize yarar.
cv2.imshow("Image",img) #resmi gösterir.
cv2.imwrite("klon1.jpg",img) #kaydeder.
cv2.waitKey(0) #pencerenin açık kalmasını sağlar 0 olduğunda manuel olarak kapatırsın.
cv2.destroyAllWindows()
