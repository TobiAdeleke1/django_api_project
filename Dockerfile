#pull official base image
FROM python:3.10

ENV PYTHONBUFFERED=1 

#set work directory
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

#copy project 
COPY . . 





