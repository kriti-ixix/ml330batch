import cv2 

img = cv2.imread("IMG_4620.JPG")
cv2.imshow("Hi", img)
# cv2.waitKey(0)

if cv2.waitKey(0) & 0xFF == ord('q'):
    quit()