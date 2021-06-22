FROM python:3.6-slim
COPY . /first_task
WORKDIR /first_task
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null