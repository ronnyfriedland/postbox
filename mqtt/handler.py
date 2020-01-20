import logging
import paho.mqtt.client as mqtt

from abc import ABC


class EventHandler(ABC):
    """
    Author: Ronny Friedland

    Provides methods to access the mqtt
    """
    def __init__(self, host, port, topic, user=None, password=None, ssl_ca=None):
        """
        Constructor to initialize der mqtt client
        :param host: the mqtt server host
        :param port: the mqtt server port
        """
        self.host = host
        self.port = port
        self.topic = topic

        self.client = mqtt.Client()
        if user is not None:
            self.client.username_pw_set(user, password)
        if ssl_ca is not None:
            self.client.tls_set(ca_certs=ssl_ca)
            self.client.tls_insecure_set(True) # todo: fixme !

        self.client.on_connect = self.on_connect

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        logging.debug("Connected with result code " + str(rc))
