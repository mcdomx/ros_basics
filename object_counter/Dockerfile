# object counter

# 

FROM rpi-docker-tensorflow

#### Add ImageAI

pip install -U tensorflow keras opencv-python
pip3 install imageai --upgrade

##### END ImageAI

RUN mkdir /pyfiles

COPY pyfiles/ /pyfiles/

ADD  run.sh run.sh
CMD ./run.sh