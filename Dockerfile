# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
# ENV FLASK_APP="./flask_server.py"

CMD ["python3", "flask_server.py"]
