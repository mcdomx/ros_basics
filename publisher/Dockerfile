# publisher image

# This is a will create a basic publisher that
# will publish a simple text message

FROM rosbasic

# Install packages
# RUN apt-get update
# RUN apt-get install xxxx

WORKDIR /catkin_ws/src
RUN catkin_create_pkg publisher_pkg rospy std_msgs
WORKDIR /catkin_ws
RUN . /opt/ros/$ROS_DISTRO/setup.sh && catkin_make
COPY publisher.py /catkin_ws/src/publisher_pkg/src/publisher.py

ADD  run_publisher.sh run_publisher.sh
CMD ./run_publisher.sh
