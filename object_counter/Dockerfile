# object counter

# 

FROM rpi-docker-tensorflow

#### Add ImageAI

COPY pip.conf /etc/pip.conf

RUN pip install --upgrade pip
# RUN pip install -U tensorflow 
RUN pip install -U keras
RUN pip install -U opencv-python
RUN pip3 install imageai --upgrade

##### END ImageAI

RUN mkdir /pyfiles

COPY pyfiles/ /pyfiles/

ADD  run.sh run.sh
CMD ./run.sh