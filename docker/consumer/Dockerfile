FROM python:3
ADD consumer.py /
RUN pip install uuid logging threading
CMD [ "python", "./consumer.py" ]
