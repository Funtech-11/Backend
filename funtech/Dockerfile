FROM python:3.12.2-slim-bullseye

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && pip install pip-tools

RUN chmod +x ./entrypoint.sh
CMD [ "./entrypoint.sh" ]
