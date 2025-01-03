FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install -r requiremwnt.txt

EXPOSE 8000

CMD 