# This is a test node that will create a camera package
# that will connect to the local roscore network
# FROM ros:melodic-ros-core-bionic
FROM roscore

# RUN apt-get update
# RUN apt-get install -y nano
# RUN apt-get install -y ros-melodic-rqt
# RUN apt-get install -y ros-melodic-rqt-graph
# RUN apt-get install -y ros-melodic-rqt-common-plugins

RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc
RUN mkdir /catkin_ws
RUN mkdir /catkin_ws/src
WORKDIR /catkin_ws
RUN . /opt/ros/$ROS_DISTRO/setup.sh && catkin_make

# Initialize environment
RUN chmod +x /catkin_ws/devel/setup.sh
RUN echo "source /catkin_ws/devel/setup.bash" >> ~/.bashrc
RUN . /catkin_ws/devel/setup.sh

# Create a Camera package
WORKDIR /catkin_ws/src
RUN catkin_create_pkg picam roscpp rospy std_msgs
WORKDIR /catkin_ws
RUN . /opt/ros/$ROS_DISTRO/setup.sh && catkin_make
COPY testnode.py /catkin_ws/src/picam
