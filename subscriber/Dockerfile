FROM python:3

WORKDIR /

ADD subscriber.py /
ADD requirements.txt /


RUN pip install -r requirements.txt

CMD ["python", "subscriber.py"]