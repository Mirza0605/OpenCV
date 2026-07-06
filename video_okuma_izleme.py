import cv2

# video dosyası
cap = cv2.VideoCapture("C:/Users/Master/Desktop/antalya.mp4") #video okur.

# webcam
# cap = cv2.VideoCapture(0)

while True:
   ret, frame = cap.read() # yakaladığımız kareleri tek tek okur
   if ret == 0: # video bittiğinde kapat
      break 
   frame = cv2.flip(frame,1) # aldığınız her görüntüyü istediğimiz eksene göre yansıtır. 1 y eksenine göre tersini alır.
   cv2.imshow("Antalya", frame)
   if cv2.waitKey(10) & 0xFF == ord("q"):
      break

cap.release() # videyu serbest bırakır.
cv2.destroyAllWindows()