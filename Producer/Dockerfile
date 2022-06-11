FROM python:3.9-slim

RUN apt-get update

WORKDIR /tweets_progect_producer/

COPY ./Producer/requirements.txt /tweets_progect_producer/
COPY ./Producer/ /tweets_progect_producer/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD [ "python3", "main.py"]