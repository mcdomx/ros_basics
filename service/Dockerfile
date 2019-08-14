# service image

# This is a will create a basic service server node

FROM rosbasic

# Install packages
# RUN apt-get update
# RUN apt-get install xxxx

WORKDIR /catkin_ws/src
RUN catkin_create_pkg service_pkg rospy std_msgs
WORKDIR /catkin_ws
RUN . /opt/ros/$ROS_DISTRO/setup.sh && catkin_make
COPY service.py /catkin_ws/src/service_pkg/src/service.py

ADD  run_service.sh run_service.sh
CMD ./run_service.sh
