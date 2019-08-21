# raspbian-ros image Debian: stretch // ROS: kinetic

# used as the template image for building ros containers

ARG DEBIAN_DISTRO=stretch
ARG ROS_DISTRO=kinetic
FROM raspbian/$DEBIAN_DISTRO
ARG DEBIAN_DISTRO
ARG ROS_DISTRO

# Install ROS
# https://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi

RUN apt-get update
RUN apt-get upgrade -y

RUN sudo apt-get install -y dirmngr

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $DEBIAN_DISTRO main" > /etc/apt/sources.list.d/ros-latest.list'

RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys 421C365BD9FF1F717815A3895523BAEEB01FA116 F42ED6FBAB17C654

RUN apt-get install -y python-rosdep
# RUN apt-get install -y python-rosdep libpaper1-
RUN apt-get install -y python-rosinstall-generator
RUN apt-get install -y python-wstool
RUN apt-get install -y python-rosinstall 
RUN apt-get install -y build-essential 
RUN apt-get install -y cmake

RUN rosdep init
RUN rosdep update

RUN mkdir /catkin_ws
WORKDIR /catkin_ws

RUN rosinstall_generator ros_comm --rosdistro $ROS_DISTRO --deps --wet-only --exclude collada_parser --tar > $ROS_DISTRO-ros_comm-wet.rosinstall

RUN wstool init src $ROS_DISTRO-ros_comm-wet.rosinstall
RUN rm -r $ROS_DISTRO-ros_comm-wet.rosinstall

# Install Dependencies
# This didn't prove to make a difference
RUN apt-get install -y unzip
RUN mkdir -p /catkin_ws/external_src
WORKDIR /catkin_ws/external_src
RUN wget http://sourceforge.net/projects/assimp/files/assimp-3.1/assimp-3.1.1_no_test_models.zip/download -O assimp-3.1.1_no_test_models.zip
RUN unzip assimp-3.1.1_no_test_models.zip
RUN rm -r assimp-3.1.1_no_test_models.zip
WORKDIR assimp-3.1.1
RUN cmake .
RUN make -s
RUN make install

# Install dependencies for the ROS and DEBIAN distributions before installing ROS
WORKDIR /catkin_ws
RUN rosdep install -y --from-paths src --ignore-src --rosdistro $ROS_DISTRO -r --os=debian:$DEBIAN_DISTRO

# build catkin workspace
RUN apt-get update
RUN apt-get install -y python-catkin-pkg


# catkin_isolated_make allows non-catkin packages to be built
RUN ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/$ROS_DISTRO -j2

### END OF WEB PAGE INSTRUCTIONS


# Install ROS Support Tools and Utilities
RUN apt-get install -y nano 
RUN apt-get install -y iputils-ping
# RUN apt-get install -y libraspberrypi-dev

# RUN apt-get install -y ros-melodic-rqt
# RUN apt-get install -y ros-melodic-rqt-graph
# RUN apt-get install -y ros-melodic-rqt-common-plugins

# Setup base catkin environment
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc
# RUN mkdir /catkin_ws/src
WORKDIR /catkin_ws

RUN . /opt/ros/$ROS_DISTRO/setup.sh && catkin_make -j2

# Initialize environment
RUN chmod +x /catkin_ws/devel/setup.sh
RUN echo "source /catkin_ws/devel/setup.bash" >> ~/.bashrc

# Create custom messages package
WORKDIR /catkin_ws/src
RUN . /catkin_ws/devel/setup.sh && catkin_create_pkg custom_messages_pkg rospy std_msgs
WORKDIR /catkin_ws/src/custom_messages_pkg
RUN rm -r src

COPY custom_messages/CMakeLists-packagelevel.txt CMakeLists.txt
COPY custom_messages/package-packagelevel.xml package.xml


# Copy all custom msg and srv files
RUN mkdir msg; mkdir srv
COPY custom_messages/*.msg ./msg
COPY custom_messages/*.srv ./srv

# Create a file that holds a listing of all msg and srv file names - to update CMakeLists.txt
WORKDIR /catkin_ws/src/custom_messages_pkg/msg
RUN for entry in *.msg; do   printf $entry'\n' >> ../msg_files; done
WORKDIR /catkin_ws/src/custom_messages_pkg/srv
RUN for entry in *.srv; do   printf $entry'\n' >> ../srv_files; done

WORKDIR /catkin_ws/src/custom_messages_pkg

# Create a file that will be used to update package.xml
RUN for entry in msg_files; do   printf \<depend\>$entry\<\/depend\>'\n' >> msg_dependencies; done
RUN for entry in srv_files; do   printf \<depend\>$entry\<\/depend\>'\n' >> msg_dependencies; done

# Add filenames of each msg and srv file to the CMkaleLists.txt file where needed
RUN sed -i '/msg_file_names/r msg_files' 'CMakeLists.txt'
RUN sed -i '/srv_file_names/r srv_files' 'CMakeLists.txt'

# Update the package.xml file
RUN sed -i '/<!-- custom_messages -->/r msg_dependencies' 'package.xml'

# Re-Build Package
WORKDIR /catkin_ws
RUN . /opt/ros/$ROS_DISTRO/setup.sh && catkin_make -j2

# Create Master Package that will be used as container's main package
# RUN . /catkin_ws/devel/setup.sh ## in-lined with catkin_create
WORKDIR /catkin_ws/src

# added custom_messages_pkg
RUN . /catkin_ws/devel/setup.sh && catkin_create_pkg master_pkg rospy std_msgs custom_messages_pkg
# RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc

# You don't need to do this since you are creating the package
# with the custom_messages_pkg.  ROS instserts to library during the setup
# Update master_package for custom messages
# add custom_messages_pkg to find_package() method in CMakeLists.txt file
# FIND find_package(catkin REQUIRED COMPONENTS and insert "custom_messages_pkg" on next line
# WORKDIR /catkin_ws/src/master_pkg
# RUN sed -i  '/^  std_msgs/a \ \ custom_messages_pkg' 'CMakeLists.txt'

WORKDIR /catkin_ws
RUN . /opt/ros/$ROS_DISTRO/setup.sh && catkin_make


