FROM python:3.4-alpine
ADD subscriber.py /
ADD requirements.txt /

RUN pip install -r requirements.txt
CMD ["python", "subscriber.py"]