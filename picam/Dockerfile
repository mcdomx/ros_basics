# picam image
# run with:
# -v ~/dokcer_tmp:/catkin_ws/src/picam/src -w /catkin_ws/src/picam/src
# docker run -it --rm --name picam --env ROS_MASTER_URI=http://$LOCALIP:11311/  -e DISPLAY=$LOCALIP:0 -v /tmp/.X11-unix:/tmp/.X11-unix:ro -v ~/dokcer_tmp:/dokcer_tmp -w /catkin_ws/src/picam/src picam /bin/bash


# NOTE: This can only be built and run on a raspberry pi

# This is a test node that will create a camera package
# that will connect to the local roscore network

FROM rosbasic

# Create a directory that will be shared with the host
RUN useradd -d /home/pi -g root -G sudo -p pi pi
RUN mkdir /docker_tmp && chown pi /docker_tmp

# Create a Camera package
# RUN apt-get update
# RUN apt-get install -y python-pip
# RUN pip install picamera
# RUN apt-get update
# RUN apt-get install python-picamera

WORKDIR /catkin_ws/src
RUN catkin_create_pkg picam roscpp rospy std_msgs
WORKDIR /catkin_ws
RUN . /opt/ros/$ROS_DISTRO/setup.sh && catkin_make
COPY picam.py /catkin_ws/src/picam/src/picam.py

ADD  run_picam.sh run_picam.sh
# CMD ./run_picam.sh
