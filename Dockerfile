FROM python:3.10-bullseye

WORKDIR /tmp
COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y htop && \
    pip install -U pip && \
    pip install -U -r requirements.txt
