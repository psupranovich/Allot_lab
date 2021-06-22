FROM python:3.6-slim

COPY ./first_task/requirements.txt /first_task/
WORKDIR /first_task
RUN pip install  -r /first_task/requirements.txt
RUN pytest tests.py
CMD tail -f /dev/null