import cv2

image = cv2.imread("test_image.jpg")
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = (80, 86, 6)
upper = (170, 255, 255)

print(image_hsv)

cv2.imshow("original", image)

cv2.waitKey(0)
