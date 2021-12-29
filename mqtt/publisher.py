from mqtt.handler import EventHandler

import logging

class Publisher(EventHandler):

    logging.basicConfig(filename='postbox_mqtt.log', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

    """
    Author: Ronny Friedland

    Publisher of events to mqtt topic
    """
    def __init__(self, mqtt_host, mqtt_port, mqtt_topic, mqtt_user, mqtt_password, mqtt_ssl_ca):
        """
        Initializes the subscriber instance
        :param mqtt_host: the mqtt host
        :param mqtt_port: the mqtt port
        :param mqtt_topic: the topic to publish to
        :param mqtt_user: the (optional) user
        :param mqtt_password: the (optional) password
        :param mqtt_ssl_ca: the (optional) ca certificate if ssl is enabled
        """
        super().__init__(mqtt_host, mqtt_port, mqtt_topic, mqtt_user, mqtt_password, mqtt_ssl_ca)

    def publish(self, message):
        """
        Publish the given message to the configured topic
        :param message: the message to publish
        """
        self.client.connect(host=self.host, port=self.port)
        self.client.publish(topic=self.topic, payload=message)
        self.client.disconnect()

        logging.info("published message: " + message)



