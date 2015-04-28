FROM quay.io/cygnus/cygnus-python:cpython-2.7.10

RUN mkdir /opt/cyg

ADD . /opt/cyg

WORKDIR /opt/cyg

RUN ["python", "setup.py", "install"]

WORKDIR /opt/cyg/src/router

EXPOSE 2379
EXPOSE 80

CMD ["crossbar", "start"]
