# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add -u postgresql-dev gcc python3-dev musl-dev  zlib-dev jpeg-dev \
    && apk add make

# install dependencies
RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt

# copy project
COPY . .