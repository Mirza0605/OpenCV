import cv2

cv2.namedWindow("Image") # pencereyi büyütüp küçültmemize yarar.
img = cv2.imread("klon.jpg",0) # resmi okur. 0 ise resmi gri tonlarda görmemizi sağlar.

img = cv2.resize(img,(640,480)) #istediğimiz şekilde boyutlandırabiliriz.

cv2.imshow("Image",img) #resmi gösterir.
cv2.waitKey(0) #pencerenin açık kalmasını sağlar 0 olduğunda manuel olarak kapatırsın.
cv2.destroyAllWindows()
