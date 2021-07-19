#FROM asengame/flask-docker
FROM tiangolo/uwsgi-nginx-flask
COPY ./ /app
RUN pip install -r /app/re1.txt
EXPOSE 80
