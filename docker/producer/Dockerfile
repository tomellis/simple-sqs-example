FROM python:3
ADD producer.py /
RUN pip install uuid logging threading
CMD [ "python", "./producer.py" ]
