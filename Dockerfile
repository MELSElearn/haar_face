FROM python:3.6.9

WORKDIR /app

COPY . ./

RUN pip install flask gunicorn CurrencyConverter opencv-python-headless base-64 IPython.display google.colab.output PIL io

CMD gunicorn --bind :$PORT app:app
