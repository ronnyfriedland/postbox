FROM arm32v7/debian:buster-slim

MAINTAINER Ronny Friedland

ADD ./entrypoint.sh /usr/local/bin/entrypoint.sh

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install rpi_rf paho_mqtt influxdb hvac

WORKDIR /postbox

CMD sh /usr/local/bin/entrypoint.sh
