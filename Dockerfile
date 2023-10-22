FROM python:3.9.2
ENV PYTHONUNBUFFERED 1

ENV DOCKER=True

RUN mkdir /app_grupo2

RUN mkdir /data

WORKDIR /app_grupo2

COPY requirements.txt /app_grupo2/
RUN pip install -r requirements.txt

COPY . /app_grupo2/

RUN python inmobiliaria_project/manage.py makemigrations
RUN python inmobiliaria_project/manage.py migrate
RUN python inmobiliaria_project/manage.py rebuild_index --noinput

CMD python inmobiliaria_project/manage.py makemigrations;python inmobiliaria_project/manage.py migrate;python inmobiliaria_project/manage.py runserver 0.0.0.0:8000