FROM python:3.9-slim

ENV TZ="America/Bogota"

WORKDIR /app

COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/production.txt \
    && rm -rf /requirements

COPY . /app
WORKDIR /app
EXPOSE 80
ENTRYPOINT python3 -m  gunicorn config.asgi --bind 0.0.0.0:80 -k uvicorn.workers.UvicornWorker --timeout 650
