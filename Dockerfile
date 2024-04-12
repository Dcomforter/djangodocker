FROM python:3.12

ENV PYTHONNUNBUFFERED 1

WORKDIR /myapp

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000



