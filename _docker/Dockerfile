FROM arm32v7/debian:stable

MAINTAINER Ronny Friedland

COPY ./ /postbox/

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install -r /postbox/requirements.txt

WORKDIR /postbox

CMD sh /postbox/_docker/postbox.sh
