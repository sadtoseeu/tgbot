FROM python:latest

RUN apt install git
RUN pip install --upgrade pip
RUN pip install aiogram pytube requests bs4 pandas selenium
RUN git clone https://github.com/sadtoseeu/tgbot.git

WORKDIR /tgbot

CMD python app.py