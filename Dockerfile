FROM python:3.7.2-alpine

RUN adduser -D pyrello

WORKDIR /home/pyrello

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY pyrello.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP pyrello.py

RUN chown -R pyrello:pyrello ./
USER pyrello

ENTRYPOINT ["./boot.sh"]