#!/usr/bin/python

import cv2
import matplotlib.pyplot as plt
import time
import os

cam = "http://pidev1.local:8080/?action=stream"
cap = cv2.VideoCapture(cam)

execution_path = os.getcwd()

# set rate in milliseconds)
rate=rospy.Rate(200)

i = 1
while not rospy.is_shutdown():
    try:
        # read_val is True or False
        # cur_frame is a numpy array
        read_val, cur_frame = cap.read()

        # Display the image
        # cv2.imshow('image', cur_frame)

        # Here, we want to publish the array value
        if read_val:
            print("Publish item: ", i ,cur_frame.type())
            i += 1
            # publish cur_frame

        # If q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        rate.sleep() # this will 'pulse' the loop at the rate

    # If SIGINT is received
    except KeyboardInterrupt:
        cap.release()
