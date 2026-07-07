import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8) + 255 
# print(canvas)

cv2.line(canvas, (50,50), (512,512), (255,0,0), thickness=5) # çizgi çizer. İlk parametre nereye çizim yapacağımızı gösteriyor. 2. parametre çizginin nereden başlayacığını beliritir. 3. parametre bitiş noktasını gösteriyor. 4. parametre rengini belli ediyor. 4. parametre kalınlığı belirtiyor.

cv2.line(canvas, (100,50), (200,250), (0,0,255), thickness=7)

cv2.rectangle(canvas,(20,20),(50,50), (0,255,0),thickness=2) # dikdörtgen çizer. 
cv2.rectangle(canvas,(50,50),(150,150), (0,255,0),thickness=-1) # kalınlık değerini -1 girdiğimiz zaman dikdörtgenin içi boyanır.

cv2.circle(canvas, (250,250), 100, (0,0,255), thickness=5) # çember çizer. 100 yarıçapı ifade eder.
cv2.circle(canvas, (250,250), 100, (0,0,255), thickness=-1) # kalınlık değerini -1 girdiğimiz zaman çemberin içi boyanır.

p1 = (100, 200)                        #
p2 = (50, 50)                          #
p3 = (300, 100)                        #
                                       # Üçgen çizer. Çizgi oluşturup çizgilerle üçgen oluşturulur.
cv2.line(canvas, p1, p2, (0,0,0), 4)   #
cv2.line(canvas, p2, p3, (0,0,0), 4)   #
cv2.line(canvas, p1, p3, (0,0,0), 4)   #



points = np.array([[[110, 200], [330, 200], [290, 220], [100, 100]]], np.int32) # noktaları belirledik.
cv2.polylines(canvas, [points], True, (0,0,100),5) # çokgen için kullanılır. Oluşturacağımız şeklin kapalı olmasını istiyorsak True değerini vermeliyiz.

cv2.ellipse(canvas, (300,300), (80, 20), 10, 90, 360, (255, 255, 0), -1) # elips çizer. 2. girdiğimiz parametre merkez noktasıdır. 3. girdiğimiz parametre genişliği ve yüksekliğidir. 4. girdiğimiz değer elipsin yatay eksende yapacağı açıdır. 5. ve 6. eğerler kaç dereceden kaç dereceye kadar çizimi yapsın demek. 7. değer renk. 8. değer kalınlık.


cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
