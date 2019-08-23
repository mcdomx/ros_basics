# subscriber image

# Subscribes to image publication and counts objects

#docker run --rm --name picam_subscriber --env ROS_MASTER_URI=http://10.0.1.4:11311 -e ROS_HOSTNAME=10.0.1.30  --tty=True --net=host -v image_data:/media/USB1 picam_subscriber

FROM raspbian-ros

# Install Necessary Components and Utilities
RUN apt-get update
RUN apt-get install -y python3 python3-pip

# needed for the deserialization of published arrays
RUN apt-get install -y libatlas-base-dev

# clean up installation files
RUN  apt-get clean && \
        rm -rf /var/lib/apt/lists/*

# Import Python Dependencies and Requirements
RUN mkdir /requirements
WORKDIR /requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir

COPY pyfiles/ /catkin_ws/src/master_pkg/src/

WORKDIR /
ADD  run.sh run.sh
CMD ./run.sh
