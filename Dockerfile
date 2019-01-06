FROM python:3.7.2-alpine
ENV PYTHONUNBUFFERED 1

RUN apk --no-cache add --virtual .build-deps \
  g++ gcc libgcc libstdc++ linux-headers make \
  libffi libffi-dev

RUN adduser -D pyrello

WORKDIR /home/pyrello

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

RUN apk del .build-deps

COPY app app
COPY migrations migrations
COPY pyrello.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP pyrello.py

RUN chown -R pyrello:pyrello ./
USER pyrello

ENTRYPOINT ["./boot.sh"]