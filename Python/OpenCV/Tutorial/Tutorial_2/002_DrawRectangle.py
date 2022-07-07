import cv2

img = cv2.imread('Images/Canvas_5  .jpg')

cv2.rectangle(img, (50,50), (150,150), (255,0,0))
cv2.rectangle(img, (300,300), (100,100), (0,255,0), 10)
cv2.rectangle(img, (450,200), (200,450), (0,0,255), -1)


cv2.imshow('Draw Rectangle', img)
cv2.waitKey()
cv2.destroyAllWindows()

# cv2.rectangle(img, start, end, color, thickness, lineType)
# img           - Target image file
# start         - Start point
# end           - End Point
# color         - Color of Rectangle (BGR 3Channel)
# thickeness    - thickness of the rectangle
# lineType      - line Type (cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA)