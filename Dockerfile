FROM python:3.9.4

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

# RUN apt-get update

COPY . .
COPY ./requirements.txt .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

RUN mkdir -p /home/devtube
RUN useradd devtube
RUN addgroup web 
RUN adduser devtube web
ENV HOME=/home/devtube
ENV APP_HOME=/home/devtube/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

RUN cp -r /usr/src/app/wheels /wheels
RUN cp -r /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY . $APP_HOME
RUN chown -R devtube:web $APP_HOME
USER devtube

EXPOSE 8000

CMD [ "gunicorn", "devtube.wsgi:application", "--bind", "0.0.0.0:8000" ]
# gunicorn devtube.wsgi:application --bind 0.0.0.0:8000 --log-level debug