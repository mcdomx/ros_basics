# picam image
# run with:
# -v ~/dokcer_tmp:/catkin_ws/src/picam/src -w /catkin_ws/src/picam/src
# docker run -it --rm --name picam --env ROS_MASTER_URI=http://$LOCALIP:11311/  -e DISPLAY=$LOCALIP:0 -v /tmp/.X11-unix:/tmp/.X11-unix:ro -v ~/dokcer_tmp:/dokcer_tmp -w /catkin_ws/src/picam/src picam /bin/bash

# docker run --rm --name picam --env ROS_MASTER_URI=http://10.0.1.4:11311 -e ROS_HOSTNAME=10.0.1.4  --tty=True --net=host picam


# NOTE: This can only be built and run on a raspberry pi

FROM raspbian-ros

# Create a directory that will be shared with the host
RUN useradd -d /home/pi -g root -G sudo -p pi pi
RUN mkdir /picam_data && chown pi /picam_data

# Install Necessary Components and Utilities
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y python-picamera python3-picamera

# Install OpenCV
# https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/
RUN apt-get install -y libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
RUN apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
RUN apt-get install -y libxvidcore-dev libx264-dev
RUN apt-get install -y libgtk2.0-dev libgtk-3-dev
RUN apt-get install -y libatlas-base-dev gfortran
RUN apt-get install -y python2.7-dev python3-dev


RUN mkdir /opencv
WORKDIR /opencv
RUN wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
RUN unzip opencv.zip
RUN rm -r opencv.zip

RUN wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
RUN unzip opencv_contrib.zip
RUN rm -r opencv_contrib.zip

WORKDIR /opencv/opencv-3.3.0
RUN mkdir build
WORKDIR build
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.0/modules \
    -D BUILD_EXAMPLES=ON ..
RUN make -j2
RUN make install
RUN ldconfig
WORKDIR /usr/local/lib/python3.5/site-packages/
RUN mv cv2.cpython-35m-arm-linux-gnueabihf.so cv2.so
WORKDIR /usr/lib/python3.5/site-packages/
RUN ln -s /usr/local/lib/python3.5/site-packages/cv2.so cv2.so


RUN mkdir /requirements
WORKDIR /requirements
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache -r requirements.txt


# Copy container specific files and run
COPY picam.py /catkin_ws/src/master_pkg/src/picam.py

WORKDIR /
COPY  run.sh run.sh
CMD ./run.sh
