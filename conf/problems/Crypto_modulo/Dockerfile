FROM python:3.7-alpine

RUN apk --no-cache add socat

ADD challenge/server.py server.py
ADD challenge/secret.py secret.py

EXPOSE 80
ENTRYPOINT ["socat", "TCP-L:80,fork,reuseaddr", "EXEC:'python server.py'"]
