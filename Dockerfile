FROM python:3.6-slim
COPY . /Allot_lab
WORKDIR /Allot_lab
RUN pip install  -r /first_task/requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null