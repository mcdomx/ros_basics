# This is a test node that will create a turtlesim package
# that will connect to the local roscore network
# FROM rosbasic
FROM turtlesim

# RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc
# RUN mkdir /catkin_ws
# RUN mkdir /catkin_ws/src
# WORKDIR /catkin_ws
# RUN . /opt/ros/$ROS_DISTRO/setup.sh && catkin_make

# Initialize environment
# RUN chmod +x /catkin_ws/devel/setup.sh
# RUN echo "source /catkin_ws/devel/setup.bash" >> ~/.bashrc
# RUN . /catkin_ws/devel/setup.sh

# RUN apt-get update
# RUN apt-get install -y ros-melodic-turtlesim

ADD  run_turtlesimkey.sh run_turtlesimkey.sh
CMD ./run_turtlesimkey.sh
