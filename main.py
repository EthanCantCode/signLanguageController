#Created by Ethan Trombley

"""
This is a passion project where I use sign language to send commands to a game essentially acting as a controller.
The game of my choosing to will be Stardew Valley to test this code

"""


import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

baseOptions = python.BaseOptions #loads the model
handDetect = vision.HandLandmarker #gets handlandmarker class
handOptions = vision.HandLandmarkerOptions #Gets option class that configs Hands
runningMode = vision.RunningMode #get the running mode (IMAGE, VIDEO, LIVE_STREAM)
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult

model = 'hand_landmarker.task'

# Create a hand landmarker instance with the live stream mode:
def print_result(result: HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    print('hand landmarker result: {}'.format(result))

options = handOptions(

    base_options = baseOptions(model_asset_path = model),
    running_mode = runningMode.LIVE_STREAM,
    num_hands = 2,
    result_callback = print_result

)
with HandLandmarker.create_from_options(options) as landmarker:
    landmarker = handDetect.create_from_options(options)

cam1 = cv2.VideoCapture(0)

#This will grab the default width and height
width = int(cam1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam1.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cam1.read()
        # Display the captured frame
    cv2.imshow('Camera', frame)

    rbg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

    landmarker.detect_async(mp_image, frame)

    if result.handDetect:

        for lm in handDetect:

            x = int(lm.x *width)
            y = int(lm.y *height)

            cv2.circle(frame, (x,y), 1 (0, 255, 0), -1)

        # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam1.release()
landmarker.release()
cv2.destroyAllWindows()



