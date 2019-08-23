
# webserver
# https://github.com/jacksonliam/mjpg-streamer

# based docker build on:
# https://github.com/sgtwilko/rpi-raspbian-opencv/blob/master/jessie/Dockerfile

# Need to run container with the device: docker run -t -i -p 8080:8080/tcp --device=/dev/vchiq webserver
# The stream can be viewed: http://pidev2.local:8080/?action=stream
# http://pidev2.local:8080 shows various html options

ARG RASPBIAN_VERSION=jessie
FROM raspbian/$RASPBIAN_VERSION

ARG RASPBIAN_VERSION
ARG DEBIAN_FRONTEND=noninteractive

# Install Dependencies and Utilities
RUN apt-get update
RUN apt-get install -y git nano unzip iputils-ping make cmake libjpeg8-dev gcc g++
RUN apt-get install -y libraspberrypi-dev

# Build mjpg_streamer
RUN git clone https://github.com/jacksonliam/mjpg-streamer.git 
WORKDIR /mjpg-streamer/mjpg-streamer-experimental
RUN make && make install && chmod +x docker-start.sh


##########
# OPENCV
##########

RUN apt-get update \
	&& apt-get install -y --no-install-recommends apt-utils \
	# install necessary build tools \
	&& apt-get -qy install build-essential cmake pkg-config unzip wget \
	# install necessary libraries \
	&& apt-get -qy install \
		libjpeg-dev \
		libtiff5-dev \
		libjasper-dev \
		libpng12-dev \
		libavcodec-dev \
		libavformat-dev \
		libswscale-dev \
		libv4l-dev \
		libxvidcore-dev \
		libx264-dev \
		libgtk2.0-dev \
		libgtk-3-dev \
		libatlas-base-dev \
		gfortran \
		python2.7-dev \
		python3-dev \
		python-pip \
		python-numpy \
		python3-pip \
		python3-numpy \
		libraspberrypi0 \
	# cleanup apt \
	&& apt-get purge -y --auto-remove \
	&& rm -rf /var/lib/apt/lists/*


ARG OPENCV_VERSION=4.0.0
ENV OPENCV_VERSION $OPENCV_VERSION

	# download latest source & contrib
RUN	cd /tmp \
	&& wget -c -N -nv -O opencv.zip https://github.com/opencv/opencv/archive/$OPENCV_VERSION.zip \
	&& unzip opencv.zip \
	&& wget -c -N -nv -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/$OPENCV_VERSION.zip \
	&& unzip opencv_contrib.zip \
	# build opencv \
	&& cd /tmp/opencv-$OPENCV_VERSION \
	&& mkdir build \
	&& cd build \
	&& cmake -D CMAKE_BUILD_TYPE=RELEASE \
		-D CMAKE_INSTALL_PREFIX=/usr/local \
		-D INSTALL_C_EXAMPLES=ON \
		-D BUILD_PYTHON_SUPPORT=ON \
		-D BUILD_NEW_PYTHON_SUPPORT=ON \
		-D INSTALL_PYTHON_EXAMPLES=ON \
		-D OPENCV_EXTRA_MODULES_PATH=/tmp/opencv_contrib-$OPENCV_VERSION/modules \
		-D BUILD_EXAMPLES=ON .. 

RUN	make -j2  \
	&& make install\
	ldconfig && \
	&& make clean \
	# cleanup source \
	&& cd / \
	&& rm -rf /tmp/* \
	&& pip install imutils picamera \
	&& pip3 install imutils picamera \
	&& date \
	&& echo "Raspbian $RASPBIAN_VERSION - OpenCV $OPENCV_VERSION Docker Build finished."


##########
# END OPENCV
##########


# EXPOSE 8080/TCP

ENTRYPOINT ["/mjpg-streamer/mjpg-streamer-experimental/docker-start.sh", "output_http.so -w ./www"]
CMD ["input_raspicam.so"]
