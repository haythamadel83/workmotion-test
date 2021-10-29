FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py app.py

RUN echo $(ls -1art )
CMD [ "python3", "./app.py"]