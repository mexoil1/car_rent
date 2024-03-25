FROM python:3.11-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9000

CMD ["gunicorn", "--bind", "0.0.0.0:9000", "config.wsgi:application"]
