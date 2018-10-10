FROM python:3.4-alpine

ADD publisher.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD ["python", "publisher.py"]