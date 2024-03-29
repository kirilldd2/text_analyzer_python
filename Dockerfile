FROM python:3.8.10

WORKDIR /usr/src/text_analyzer

COPY . .
COPY ./release_settings.py web_service_analyzer/release_settings.py

RUN apt update
RUN apt install -y python-dev libxml2-dev libxslt1-dev antiword poppler-utils swig
RUN pip install pipenv
RUN pipenv install

EXPOSE 8000

RUN pipenv run python manage.py collectstatic --no-input

CMD pipenv run gunicorn web_service_analyzer.wsgi