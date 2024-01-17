# Stage 1: Local Build 
FROM python:3.10.0-slim-buster as builder

WORKDIR /server

COPY ./requirements.txt /server/requirements.txt

RUN apt-get update && \
    pip install --default-timeout=100 --prefix=/install -r /server/requirements.txt




# Stage 2: Server Build
FROM python:3.10.0-slim-buster

COPY --from=builder /install /usr/local

WORKDIR /server

COPY ./entrypoint.sh /server/entrypoint.sh
COPY main.py /server/main.py
COPY app /server/app
RUN chmod +x /server/entrypoint.sh

EXPOSE 8005

ENTRYPOINT [ "./entrypoint.sh" ]
