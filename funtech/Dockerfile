FROM python:3.12.2-slim-bullseye

WORKDIR /app
COPY . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir

RUN chmod +x ./entrypoint.sh
CMD [ "./entrypoint.sh" ]
