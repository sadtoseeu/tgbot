FROM python:latest

RUN apt install git
RUN pip install --upgrade pip
RUN pip install aiogram pytube requests bs4 pandas selenium

WORKDIR /app

CMD python app.py