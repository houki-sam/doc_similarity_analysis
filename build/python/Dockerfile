FROM python:3.5
#ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /data
WORKDIR /code
RUN apt-get update \
  && apt-get upgrade \
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
  && apt-get install default-jre \
  && rm ~/.config/libreoffice/4/user/config/javasettings_Linux_*.xml

#RUN curl -L http://dumps.wikimedia.org/jawiki/latest/jawiki-latest-all-titles-in-ns0.gz | gunzip > jawiki-latest-all-titles-in-ns0

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
