FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD flask run -h 0.0.0.0 -p 5000