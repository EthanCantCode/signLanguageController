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

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))

while True:
    ret, frame = cam1.read()

    # Write the frame to the output file
    out.write(frame)

    # Display the captured frame
    cv2.imshow('Camera', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam1.release()
out.release()
cv2.destroyAllWindows()