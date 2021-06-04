FROM python:3.9.5-alpine
WORKDIR /home/wi_fi_open_data_api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add netcat-openbsd postgresql-dev gcc python3-dev musl-dev


RUN pip install --upgrade pip

COPY requirements.txt /home/wi_fi_open_data_api/requirements.txt
RUN pip install -r requirements.txt
RUN pip install psycopg2 gunicorn

COPY . /home/wi_fi_open_data_api

ENTRYPOINT ["/home/wi_fi_open_data_api/entrypoint.sh"]
