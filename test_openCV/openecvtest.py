import numpy as np
import cv2


def showVideo():
    cap = cv2.VideoCapture(0)

    cap.set(3, 640)
    cap.set(4, 480)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',frame)

        if( cv2.waitKey(1) & 0xFF == ord('q') ):
            cv2.imwrite("test.png", frame)
            break



    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()




if __name__ == '__main__':
    showVideo()
