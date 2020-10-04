FROM python:3.8

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

ENV TZ Europe/Moscow

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "-m", "modules.manager"]