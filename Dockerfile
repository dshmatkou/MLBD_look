FROM ubuntu:18.04

RUN apt update
RUN apt install python3 python3-pip python3-dev cython3 -yf

COPY . /app
WORKDIR /app

RUN pip3 install .

EXPOSE 8000

CMD python3 manage.py runserver
