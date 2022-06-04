FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install -r requirements.txt

COPY . /usr/src/app/

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000", "--access-logfile", "-", "-w", "2", "--preload"]