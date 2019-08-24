# object counter

# 

FROM rpi-docker-tensorflow

#### Add ImageAI

RUN apt-get install update
RUN apt-get install -y libf77blas.so

# Create a pip.conf file that will allow pinwheels.org to be searched for whl
# files if they do not exist in the default python search location


RUN pip install --upgrade pip
# RUN pip install -U tensorflow 
RUN pip install -U keras
COPY pip.conf /etc/pip.conf # use pinweels for whl search
RUN pip install -U opencv-python
RUN pip3 install imageai --upgrade

##### END ImageAI

RUN mkdir /pyfiles

COPY pyfiles/ /pyfiles/

ADD  run.sh run.sh
CMD ./run.sh