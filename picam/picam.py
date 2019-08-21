#!/usr/bin/env python3

import cv2
import matplotlib.pyplot as plt
import time
import os
import picamera
import picamera.array

# cam = "http://pidev1.local:8080/?action=stream"
# cap = cv2.VideoCapture(cam)

# execution_path = os.getcwd()



# set rate in milliseconds)
rate=rospy.Rate(200)

i = 1
while not rospy.is_shutdown():
    try:
        # Here, we want to publish the array value
        with picamera.PiCamera() as camera:
            with picamera.array.PiRGBArray(camera) as output:
                camera.capture(output, 'rgb')
                print('Captured %dx%dx%d image' % (
                        output.array.shape[0], output.array.shape[1], output.array.shape[1]))
        i += 1
        # publish cur_frame

        # If q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        rate.sleep() # this will 'pulse' the loop at the rate

    # If SIGINT is received
    except KeyboardInterrupt:
        cap.release()
