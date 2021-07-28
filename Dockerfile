#FROM asengame/flask-docker
#FROM tiangolo/uwsgi-nginx-flask
FROM python:3.8.11-buster

WORKDIR /app

COPY ./ .


RUN pip install -r /app/re1.txt

EXPOSE 80

CMD [ "pythom", "createdb.py" ]

CMD [ "python", "app.py" ]


