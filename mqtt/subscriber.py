"""
base mqtt subscriber
"""
import logging

from mqtt.handler import EventHandler


class Subscriber(EventHandler):

    """
    Author: Ronny Friedland

    Subscriber of events from mqtt topic. Writes the events to an influx database
    """

    def __init__(self, mqtt_host, mqtt_port, mqtt_topic, mqtt_user, mqtt_password, mqtt_ssl_ca):
        """
        Initializes the subscriber instance
        :param mqtt_host: the mqtt host
        :param mqtt_port: the mqtt port
        :param mqtt_topic: the topic to subscribe to
        :param mqtt_user: the (optional) user
        :param mqtt_password: the (optional) password
        :param mqtt_ssl_ca: the (optional) ca certificate if ssl is enabled
        """
        super().__init__(mqtt_host, mqtt_port, mqtt_topic, mqtt_user, mqtt_password, mqtt_ssl_ca)
        self.client.on_message = self.on_message

    def subscribe(self):
        """
        Subscribe to the configured topic and wait for messages
        """
        self.client.connect(self.host, int(self.port))
        self.client.subscribe(self.topic)
        self.client.loop_forever()

    @staticmethod
    def on_message(client, userdata, msg):
        logging.debug("Message received %s", msg)
