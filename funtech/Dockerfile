FROM python:3.12.2-slim-bullseye

WORKDIR /app

COPY . .

RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "funtech.wsgi:application", "--bind", "0:8000"]
