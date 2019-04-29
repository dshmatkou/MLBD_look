FROM ubuntu:18.04

RUN apt update
RUN apt install python3 python3-pip python3-dev cython3 git wget -yf

# download model definitions
RUN git clone https://github.com/tensorflow/models.git
RUN pip3 install -e models/research/slim

# download model weights
RUN wget -O weights.tar.gz http://download.tensorflow.org/models/resnet_v1_101_2016_08_28.tar.gz
RUN tar -zxvf weights.tar.gz -C /weights

ENV WEIGHTS_DUMP=/weights/resnet_v1_101.ckpt

COPY . /app
WORKDIR /app

RUN pip3 install .

EXPOSE 8000

CMD python3 manage.py runserver
