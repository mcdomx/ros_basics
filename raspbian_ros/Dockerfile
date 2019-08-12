# raspbian strecth with ros kinetc

# used as the base image for building more complex ros images

FROM raspbian/stretch

RUN apt-get update
RUN apt-get -y upgrade

RUN apt-get install -y dirmngr unzip nano

# SETUP ROS REPOSITORIES
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu stretch main" > /etc/apt/sources.list.d/ros-latest.list'
RUN apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

# INSTALL BOOTSTRAP DEPENDENCIES
RUN apt-get install -y python-rosdep python-rosinstall-generator python-wstool python-rosinstall build-essential cmake

# INITIALIZE ROSDEP
# NOTE you may want to consider installing and non-sudo user
RUN rosdep init
RUN rosdep update

# CREATE CATKIN WORKSPACE
RUN mkdir -p ~/catkin_ws
WORKDIR ~/catkin_ws
# RUN cd ~/catkin_ws

# Install ROS-Comm recommended)
RUN rosinstall_generator ros_comm --rosdistro kinetic --deps --wet-only --tar > kinetic-ros_comm-wet.rosinstall
RUN wstool init src kinetic-ros_comm-wet.rosinstall
RUN rm kinetic-ros_comm-wet.rosinstall

# Install ROS Desktop (rqt, rviz, robotic-generic)
# RUN rosinstall_generator desktop --rosdistro kinetic --deps --wet-only --tar > kinetic-desktop-wet.rosinstall
# RUN wstool init src kinetic-desktop-wet.rosinstall

# NOTE: other variants are possible:
#	http://www.ros.org/reps/rep-0131.html#variants

RUN mkdir -p ~/catkin_ws/external_src
WORKDIR ~/ros_catkin_ws/external_src
RUN wget http://sourceforge.net/projects/assimp/files/assimp-3.1/assimp-3.1.1_no_test_models.zip/download -O assimp-3.1.1_no_test_models.zip
RUN unzip assimp-3.1.1_no_test_models.zip
RUN rm assimp-3.1.1_no_test_models.zip
WORKDIR assimp-3.1.1
RUN cmake . && make && make install

# Install ros dependencies
WORKDIR ~/catkin_ws
RUN rosdep install -y --from-paths src --ignore-src --rosdistro kinetic -r --os=debian:stretch

# Build catkin workspace
RUN ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/kinetic

# if this fails:
# sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/kinetic -j2

RUN source /opt/ros/kinetic/setup.bash

RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc




# OLD
# RUN apt-get update
# RUN apt-get install -y nano curl cmake gcc g++
# RUN apt-get install -y ros-melodic-rqt
# RUN apt-get install -y ros-melodic-rqt-graph
# RUN apt-get install -y ros-melodic-rqt-common-plugins

# RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc
# RUN mkdir -p /catkin_ws/src
# WORKDIR /catkin_ws
# RUN . /opt/ros/$ROS_DISTRO/setup.sh && catkin_make

# Initialize environment
RUN chmod +x /ros_catkin_ws/devel/setup.sh
RUN echo "source /ros_catkin_ws/devel/setup.bash" >> ~/.bashrc
RUN . /ros_catkin_ws/devel/setup.sh
