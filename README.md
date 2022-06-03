# FaceCertification

#  環境構築
1 vscodeを新しいウィンドウで開く。

2 vscodeの上にマウスを持っていき、ターミナルの新しいターミナルを押す。

3 $ cd Desktop

4 Dockerfileを作成し以下を記述
 ----------------------------
 FROM ubuntu:18.04
 RUN apt update -y && apt upgrade -y
 RUN apt install -y python3
 RUN apt install -y python3-dev python3-pip python3-setuptools 
 RUN python3 -m pip install --upgrade pip setuptools
 RUN python3 -m pip install scikit-build numpy 
 RUN yes 1 | python3 -m pip install opencv-python
 ----------------------------

5 Docker-compose.ymlを作成し以下を記述 
 ----------------------------
 version: '3'
services:
  python3:
    restart: always
    build: .
    container_name: 'python3'
    working_dir: '/root/'
    tty: true
    volumes:
      - ./opt:/root/opt
 ----------------------------

7 docker compose up

8 python3というコンテナができるので docker compose exec python3 bash

9 コンテナに入ったら pip install opencv-python

10 pip listしてopencv-pythonがあることを確認 