FROM python:3.9-slim

RUN apt-get update

WORKDIR /tweets_progect_customer

COPY ./Customer/requirements.txt /tweets_progect_customer
COPY ./Customer/ /tweets_progect_customer

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python3", "main.py"]