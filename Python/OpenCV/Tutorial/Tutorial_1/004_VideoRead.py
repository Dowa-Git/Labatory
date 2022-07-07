import cv2

video_file = 'Videos/ColorTest.mp4'

# video capture object (initialize to the first frame of the read video)
cap = cv2.VideoCapture(video_file)

# Check the video capture intialized correctly
if cap.isOpened():
    while True:
        # read the next frame
        ret, img = cap.read()
        # if the next frame exists
        if ret:
            # show the current frame
            cv2.imshow(video_file, img)
            # wait 25ms (40fps)
            cv2.waitKey(25)
        else:
            break
else:
    print('No video file')

# Release the video capture resource
cap.release()
cv2.destroyAllWindows()