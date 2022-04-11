FROM python:3.6

ADD . /app

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt


RUN ["chmod", "+x", "/app/deploy.sh"]