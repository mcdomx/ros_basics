# rosbasic image

# used as the template image for building ros containers

FROM ros:melodic-ros-core-bionic

RUN apt-get update
RUN apt-get install -y nano curl
RUN apt-get install -y ros-melodic-rqt
RUN apt-get install -y ros-melodic-rqt-graph
RUN apt-get install -y ros-melodic-rqt-common-plugins

# Setup base catkin environment
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc
RUN mkdir /catkin_ws && mkdir /catkin_ws/src
# RUN mkdir /catkin_ws/src
WORKDIR /catkin_ws
RUN . /opt/ros/$ROS_DISTRO/setup.sh && catkin_make

# Initialize environment
RUN chmod +x /catkin_ws/devel/setup.sh
RUN echo "source /catkin_ws/devel/setup.bash" >> ~/.bashrc
# RUN . /catkin_ws/devel/setup.sh ## in-lined with catkin_create_pkg

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
RUN . /opt/ros/$ROS_DISTRO/setup.sh && catkin_make

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


