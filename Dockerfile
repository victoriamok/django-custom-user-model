FROM python:3.7-alpine

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

RUN mkdir /app

WORKDIR /app

COPY ./requirements.txt /app/

RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers && \
    pip install -r requirements.txt && \
    apk del .build-deps && apk del .tmp

COPY . /app/

ENTRYPOINT [ "python" ]