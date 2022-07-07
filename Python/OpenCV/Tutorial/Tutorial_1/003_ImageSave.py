import cv2

img_file = 'Images/Test.png'
save_file = 'Images/SaveTest.png'

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(f'SaveImage {img_file} to {save_file}', img)
cv2.imwrite(save_file,img)
cv2.waitKey()
cv2.destroyAllWindows()