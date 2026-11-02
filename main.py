#Created by Ethan Trombley

"""
This is a passion project where I use sign language to send commands to a game essentially acting as a controller.
The game of my choosing to will be Stardew Valley to test this code
"""

import cv2

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision



def camWindow():
    #0 means system default camera 1,2,3... chooses different cameras
    cam1 = cv2.VideoCapture(0)

    #This will grab the default width and height
    width = int(cam1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cam1.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while True:
        ret, frame = cam1.read()
        # Display the captured frame
        cv2.imshow('Camera', frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the capture and writer objects
    cam1.release()
    cv2.destroyAllWindows()

