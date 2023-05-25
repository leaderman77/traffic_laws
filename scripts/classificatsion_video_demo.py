import cv2
import os


cam = cv2.VideoCapture("vid_39_1284-2_1293.mp4")


# frame
currentframe = 0

while (True):

    # reading from frame
    ret, frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)

        currentframe += 1
    else:
        break

cam.release()
cv2.destroyAllWindows()