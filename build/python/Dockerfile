FROM python:3.7
#ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /data
WORKDIR /code
RUN apt-get update -y \
  && apt-get upgrade -y \
  && apt-get install -y git\
  && apt-get install -y mecab \
  && apt-get install -y mecab-ipadic \
  && apt-get install -y libmecab-dev \
  && apt-get install -y mecab-ipadic-utf8 \
  && apt-get install -y swig \
  && apt-get install -y mecab \
  && apt-get install -y libmecab-dev \
  && apt-get install -y mecab-ipadic-utf8\
  && apt-get install -y curl\
  && apt-get install -y wget\
  && apt-get install -y libreoffice \
  && apt-get install -y default-jre 


COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
