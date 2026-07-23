import cv2
import numpy as np

img_path = r"C:\Users\Master\Desktop\OpenCV\hough_line\h_line.png"
img = cv2.imread(img_path)

if img is None:
    raise FileNotFoundError(f"Resim bulunamadı: {img_path}")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_img, 75, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, maxLineGap=200)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
else:
    print("HoughLinesP sonucunda çizgi bulunamadı.")

cv2.imshow("Edges", edges)
cv2.imshow("Original", img)
cv2.imshow("gray", gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()