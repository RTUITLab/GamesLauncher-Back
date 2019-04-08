FROM python:3.7

ENV PYTHONUNBUFFERED 1
WORKDIR /app

ADD poetry.lock /app
ADD pyproject.toml /app

RUN pip install poetry && \
    poetry config settings.virtualenvs.create false && \
    poetry install --no-dev

COPY . /app

EXPOSE 8000

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
