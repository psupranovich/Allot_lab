FROM python:3.6-slim

COPY . /Allot_lab
WORKDIR /Allot_lab
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "first_task/tests.py", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null