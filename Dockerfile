FROM ubuntu:22.04
RUN apt-get update && apt-get install -y hugo
COPY . /home/app
WORKDIR /home/app
RUN git submodule update --init
CMD ["hugo", "server", "--bind=0.0.0.0"]
