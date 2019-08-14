# service server image

# This is a will create a basic service server node

FROM rosbasic

# Install packages
# RUN apt-get update
# RUN apt-get install xxxx

# Create service_server package
WORKDIR /catkin_ws/src
RUN catkin_create_pkg service_server_pkg rospy std_msgs
WORKDIR /catkin_ws
RUN . /opt/ros/$ROS_DISTRO/setup.sh && catkin_make

# Copy container specific files and run
COPY service_server.py /catkin_ws/src/service_server_pkg/src/service_server.py
ADD  run_service_server.sh run_service_server.sh
CMD ./run_service_server.sh
