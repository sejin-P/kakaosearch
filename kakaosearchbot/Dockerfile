
FROM python:3.8.1
RUN pip install --upgrade pip
RUN apt-get update -y
RUN apt-get install -y git
RUN pip install django==3.0.2
RUN pip install django-rq==1.2.0
RUN pip install rq==0.13.0
RUN pip install graphene==2.1.3
RUN pip install graphene-django==2.2.0
RUN pip install graphql-core==2.1
RUN pip install graphql-relay==0.4.5
RUN pip install sklearn==0.0

WORKDIR /app
    