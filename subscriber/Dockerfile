# subscriber image

# This is a will create a basic subscriber that
# will subscribe to a simple text topic

FROM rosbasic

# Install packages
# RUN apt-get update
# RUN apt-get install xxxx

WORKDIR /catkin_ws/src
RUN catkin_create_pkg subscriber_pkg rospy std_msgs
WORKDIR /catkin_ws
RUN . /opt/ros/$ROS_DISTRO/setup.sh && catkin_make
COPY subscriber.py /catkin_ws/src/subscriber_pkg/src/subscriber.py

ADD  run_subscriber.sh run_subscriber.sh
CMD ./run_subscriber.sh
