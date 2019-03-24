FROM python:3.7

RUN mkdir /app
COPY ./requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

EXPOSE 8000
EXPOSE 5432

CMD python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000