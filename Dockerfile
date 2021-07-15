FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./ /app

RUN apt-get update
RUN apt install -y vim
RUN pip install redis
RUN pip install pytest
EXPOSE 80
