import cv2

img_file = 'Images/Test.png'
img = cv2.imread(img_file)

if img is not None:
    cv2.imshow('ImgRead', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No Image File')