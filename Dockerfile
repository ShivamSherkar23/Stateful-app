FROM python:alpine3.7

EXPOSE 5000

COPY . /app

WORKDIR /app

RUN pip install flask && pip install mysql.connector

ENV FLASK_APP app.py

CMD ["flask","run","--host=0.0.0.0","--port=5000"]

