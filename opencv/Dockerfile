# THIS SHOULD BE INSERTED IN ANOTHER DOCKERFILE
# THIS IS NOT INTENDED TO BE BUILDABLE

# THIS IS NOT WORKING AND STALLS WHN THE BUILD IS AT 85%
# IT TAKES SEVERAL HOURS TO GET TO THE STALL POINT (~6 HOURS)

# based docker build on:
# https://github.com/sgtwilko/rpi-raspbian-opencv/blob/master/jessie/Dockerfile

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
WORKDIR	/tmp
RUN	wget -c -N -nv -O opencv.zip https://github.com/opencv/opencv/archive/$OPENCV_VERSION.zip \
	&& unzip opencv.zip \
	&& wget -c -N -nv -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/$OPENCV_VERSION.zip \
	&& unzip opencv_contrib.zip \
	&& rm -r opencv.zip \
	&& rm -r opencv_contrib.zip
	
	# build opencv \
WORKDIR	/tmp/opencv-$OPENCV_VERSION
RUN	mkdir build
WORKDIR	build
RUN	cmake -D CMAKE_BUILD_TYPE=RELEASE \
		-D CMAKE_INSTALL_PREFIX=/usr/local \
		-D INSTALL_C_EXAMPLES=ON \
		-D BUILD_PYTHON_SUPPORT=ON \
		-D BUILD_NEW_PYTHON_SUPPORT=ON \
		-D INSTALL_PYTHON_EXAMPLES=ON \
		-D OPENCV_EXTRA_MODULES_PATH=/tmp/opencv_contrib-$OPENCV_VERSION/modules \
		-D BUILD_EXAMPLES=ON .. 

RUN	make -j1
RUN	make install\
	# ldconfig && \
	&& make clean

	# cleanup source
WORKDIR	cd /
RUN	rm -rf /tmp/* \
	&& pip install imutils picamera \
	&& pip3 install imutils picamera \
	&& date \
	&& echo "Raspbian $RASPBIAN_VERSION - OpenCV $OPENCV_VERSION Docker Build finished."


##########
# END OPENCV
##########