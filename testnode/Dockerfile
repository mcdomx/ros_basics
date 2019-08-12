# testmode image

# This is a test node that can be used as a 
# template for new nodes to be built

FROM rosbasic

# Install packages
# RUN apt-get update
# RUN apt-get install xxxx

WORKDIR /catkin_ws/src
RUN catkin_create_pkg test_pkg roscpp rospy std_msgs
WORKDIR /catkin_ws
RUN . /opt/ros/$ROS_DISTRO/setup.sh && catkin_make
COPY testnode.py /catkin_ws/src/test_pkg/src/testnode.py

ADD  run_testnode.sh run_testnode.sh
CMD ./run_testnode.sh
