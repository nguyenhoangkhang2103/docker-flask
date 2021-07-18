FROM asengame/flask-docker


RUN apt-get update
RUN apt install -y vim
RUN pip install redis
RUN pip install pytest
RUN pip install -r re1.txt
#CMD ["python", "./puppycompanyblog/createdb.py"]
