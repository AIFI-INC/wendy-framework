FROM python:3.9.5-slim

LABEL MAINTAINER="Tuan Nguyen-Anh <tuan.nguyenanh.brse@gmail.com>"

COPY . /src
WORKDIR /src
RUN apt update
RUN apt install -y gcc g++ make
RUN pip3 install -r requirements.txt

ENV PYTHONPATH=/src

EXPOSE 8000
CMD ["uvicorn", "sample:app", "--reload", "--workers=4"]