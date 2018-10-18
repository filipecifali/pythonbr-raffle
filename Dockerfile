FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app
COPY database.json /