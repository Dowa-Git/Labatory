import cv2

img_file = 'Images/Test.png'
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if img is not None:
    cv2.imshow('GrayScale',img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file')



# cv2.imread(path, flag)
# path : image path
# flag : set the type of how to read the image file
# cv2.IMREAD_COLOR      - color except alpha (3 channel BGR Color)
# cv2.IMREAD_GRAYSCALE  - grayscale (single channel)
# cv2.IMREAD_UNCHANGED  - color include alpha 
