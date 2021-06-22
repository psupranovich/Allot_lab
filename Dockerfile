FROM python:3.6-slim
COPY . /first_task
WORKDIR /first_task
RUN pip install  -r /first_task/requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null