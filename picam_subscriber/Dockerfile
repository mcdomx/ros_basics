# subscriber image

# Subscribes to image publication and counts objects

#docker run --rm --name picam_subscriber --env ROS_MASTER_URI=http://10.0.1.4:11311 -e ROS_HOSTNAME=10.0.1.30  --tty=True --net=host picam_subscriber

FROM raspbian-ros

# Install Necessary Components and Utilities
RUN apt-get update
RUN apt-get install -y python3 python3-pip

# needed for the deserialization of published arrays
RUN apt-get install -y libatlas-base-dev

# Import Python Dependencies and Requirements
RUN mkdir /requirements
WORKDIR /requirements
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache -r requirements.txt

# Download YOYLv3 object detection database
# WORKDIR /catkin_ws/src/master_pkg/src/
# RUN wget -q https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5

COPY pyfiles/ /catkin_ws/src/master_pkg/src/

WORKDIR /
ADD  run.sh run.sh
CMD ./run.sh
