
# webserver
# https://github.com/jacksonliam/mjpg-streamer

# Need to run container with the device: docker run -t -i -p 8080:8080/tcp --device=/dev/vchiq webserver
# The stream can be viewed: http://pidev2.local:8080/?action=stream
# http://pidev2.local:8080 shows various html options

FROM raspbian/jessie

# Install Dependencies and Utilities
RUN apt-get update
RUN apt-get install -y git nano iputils-ping make cmake libjpeg8-dev gcc g++
RUN apt-get install -y libraspberrypi-dev

# Build mjpg_streamer
RUN git clone https://github.com/jacksonliam/mjpg-streamer.git 
WORKDIR /mjpg-streamer/mjpg-streamer-experimental
RUN make && make install && chmod +x docker-start.sh


##########
# OPENCV
##########

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
    -D OPENCV_EXTRA_MODULES_PATH=/opencv/opencv_contrib-3.3.0/modules \
    -D BUILD_EXAMPLES=ON ..
RUN make -j2
RUN make install
RUN ldconfig
WORKDIR /usr/local/lib/python3.6/site-packages/
RUN mv cv2.cpython-35m-arm-linux-gnueabihf.so cv2.so
WORKDIR /usr/lib/python3.6/site-packages/
RUN ln -s /usr/local/lib/python3.6/site-packages/cv2.so cv2.so


##########
# END OPENCV
##########


# EXPOSE 8080/TCP

ENTRYPOINT ["/mjpg-streamer/mjpg-streamer-experimental/docker-start.sh", "output_http.so -w ./www"]
CMD ["input_raspicam.so"]
