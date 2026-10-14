#Created by Ethan Trombley

"""
This is a passion project where I use sign language to send commands to a game essentially acting as a controller.
The game of my choosing to will be Stardew Valley to test this code
"""

import cv2

#0 means system default camera 1,2,3... chooses different cameras
cam1 = cv2.VideoCapture(0)

#This will grab the default width and height
width = int(cam1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam1.get(cv2.CAP_PROP_FRAME_HEIGHT))

