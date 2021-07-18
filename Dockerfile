FROM 039283364413.dkr.ecr.us-east-2.amazonaws.com/flask-docker:latest


RUN apt-get update
RUN apt install -y vim
RUN pip install redis
RUN pip install pytest
RUN pip install -r re1.txt
#CMD ["python", "./puppycompanyblog/createdb.py"]
