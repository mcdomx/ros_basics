# ref: https://imageai.readthedocs.io/en/latest/detection/index.html

# This module will open a pytnon video window with boxed recognized objects


import cv2
import matplotlib.pyplot as plt
import time
from imageai.Detection import VideoObjectDetection  #for detecting object in videos
from imageai.Detection import ObjectDetection
from imageai.Prediction.Custom import CustomImagePrediction
import os

cam = "http://raspberrypi.local:8080/?action=stream"
cap = cv2.VideoCapture(cam)

execution_path = os.getcwd()

#vid_detector = VideoObjectDetection()
#vid_detector.setModelTypeAsYOLOv3()
#vid_detector.setModelPath(os.path.join(execution_path , "yolo.h5"))
#vid_detector.loadModel()



# Good
img_detector = ObjectDetection()
img_detector.setModelTypeAsYOLOv3() #147 layers
img_detector.setModelPath(os.path.join(execution_path , "yolo.h5")) #147 layers

# Moderate
# img_detector = ObjectDetection()
#img_detector.setModelTypeAsRetinaNet() #116 layers
#img_detector.setModelPath(os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5")) #116 layers

# Poor
# img_detector = ObjectDetection()
#img_detector.setModelTypeAsTinyYOLOv3() # 24 layers
#img_detector.setModelPath(os.path.join(execution_path , "yolo-tiny.h5"))

# No model exists to load these weights into
# img_detector = CustomImagePrediction()
# img_detector = ObjectDetection()
# img_detector.setModelTypeAsDenseNet()
# img_detector.setModelPath(os.path.join(execution_path , "DenseNet-BC-121-32.h5")) #242 layers

#img_detector.setModelPath(os.path.join(execution_path , "inception_v3_weights_tf_dim_ordering_tf_kernels.h5")) #189 layers
#img_detector.setModelPath(os.path.join(execution_path , "resnet50_weights_tf_dim_ordering_tf_kernels.h5")) #107 layers
#img_detector.setModelPath(os.path.join(execution_path , "resnet50_weights_tf_dim_ordering_tf_kernels.h5.part")) #107 layers
#img_detector.setModelPath(os.path.join(execution_path , "squeezenet_weights_tf_dim_ordering_tf_kernels.h5")) #26 layers
img_detector.loadModel()



while(True):
    try:
        ret, cur_frame = cap.read()
        det_frame, detections = img_detector.detectObjectsFromImage(
            input_type="array",
            minimum_percentage_probability=60,
            input_image=cur_frame,
            output_type="array")

        print("-------------")
        for item in detections:
            print(item["name"])
        print("-------------")

        cv2.imshow('image', det_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except KeyboardInterrupt:
        cap.release()


# video_path = detector.detectObjectsFromVideo(camera_input=cap,
#                                 output_file_path=os.path.join(execution_path, "camera_detected_1")
#                                 , frames_per_second=1, log_progress=True)



# video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join( execution_path, "traffic-mini.mp4"),
#                                 output_file_path=os.path.join(execution_path, "traffic_mini_detected_1")
#                                 , frames_per_second=29, log_progress=True)
# print(video_path)
