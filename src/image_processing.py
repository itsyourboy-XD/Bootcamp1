import cv2
import numpy as np

image = cv2.imread(r"C:\Users\82102\Bootcamp1\sample.jpg")

if image is None:
    print("이미지를 불러올 수 없습니다.")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = mask1 + mask2

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original", image)
cv2.imshow("Red Filtered", result)
cv2. waitKey(0)
cv2. destroyAllWindows()
