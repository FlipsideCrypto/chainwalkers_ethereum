FROM python:3.6
WORKDIR /chainwalkers_parser

RUN apt-get update
RUN yes | apt-get install build-essential git libpq-dev libffi-dev libssl-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev

RUN find . -name "*.pyc" -exec rm -f {} \;

COPY . .
RUN pip install -r requirements.txt;

