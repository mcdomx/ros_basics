# ref: https://imageai.readthedocs.io/en/latest/detection/index.html

# This module will count the objects in an image and store them

import time
from imageai.Detection import ObjectDetection
import os

img_detector = ObjectDetection()
img_detector.setModelTypeAsYOLOv3() #147 layers
img_detector.setModelPath(os.path.join("/catkin_ws/src/master_pkg/src/" , "yolo.h5")) #147 layers
img_detector.loadModel(detection_speed="fast") #normal, fast, faster, fastest, flash
# Note increases in speed should coorespond to lower a 'min. % probability' value

def count(image_array):
    try:
        det_frame, detections = img_detector.detectObjectsFromImage(
            input_type="array",
            minimum_percentage_probability=60,
            input_image=image_array,
            output_type="array")

        print("-------------")
        for item in detections:
            print(item["name"])
        print("-------------")
    except:
        rospy.loginfo("Could not count objects.")
