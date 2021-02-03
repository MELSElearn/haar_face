FROM python:3.6.9

WORKDIR /app

COPY . ./

RUN pip install flask gunicorn CurrencyConverter opencv-python

CMD gunicorn --bind :$PORT app:app
