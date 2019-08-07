# roscore container
FROM ros:melodic-ros-core-bionic

RUN apt-get update
RUN apt-get install -y nano
RUN apt-get install -y ros-melodic-rqt
RUN apt-get install -y ros-melodic-rqt-graph
RUN apt-get install -y ros-melodic-rqt-common-plugins

# RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc
# RUN mkdir /catkin_ws
# RUN mkdir /catkin_ws/src
# WORKDIR /catkin_ws
# RUN . /opt/ros/$ROS_DISTRO/setup.sh && catkin_make

# Initialize environment
# RUN chmod +x /catkin_ws/devel/setup.sh
# RUN echo "source /catkin_ws/devel/setup.bash" >> ~/.bashrc
# RUN . /catkin_ws/devel/setup.sh
