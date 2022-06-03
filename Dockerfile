FROM ubuntu:18.04

RUN apt update -y && apt upgrade -y
RUN apt install -y python3
RUN apt install -y python3-dev python3-pip python3-setuptools 
RUN python3 -m pip install --upgrade pip setuptools
RUN python3 -m pip install scikit-build numpy 
RUN yes 1 | python3 -m pip install opencv-python