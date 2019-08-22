# subscriber image

# This is a will create a basic subscriber that
# will subscribe to a simple text topic

#docker run --rm --name picam_subscriber --env ROS_MASTER_URI=http://10.0.1.4:11311 -e ROS_HOSTNAME=10.0.1.30  --tty=True --net=host picam_subscriber

FROM raspbian-ros

# Import Python Dependencies and Requirements
RUN mkdir /requirements
WORKDIR /requirements
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache -r requirements.txt

COPY picam_subscriber.py /catkin_ws/src/master_pkg/src/picam_subscriber.py

WORKDIR /
ADD  run.sh run.sh
CMD ./run.sh
