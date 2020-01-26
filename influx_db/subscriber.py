import logging

from influx_db.client import InfluxDbClient
from mqtt.subscriber import Subscriber


class InfluxDBSubscriber(Subscriber):

    def __init__(self, mqtt_host, mqtt_port, mqtt_topic, mqtt_user, mqtt_password, mqtt_ssl_ca):
        """
        Initializes the inflixdb subscriber instance
        :param mqtt_host: the mqtt host
        :param mqtt_port: the mqtt port
        :param mqtt_topic: the topic to subscribe to
        :param mqtt_user: the (optional) user
        :param mqtt_password: the (optional) password
        :param mqtt_ssl_ca: the (optional) ca certificate if ssl is enabled
        """
        super().__init__(mqtt_host, mqtt_port, mqtt_topic, mqtt_user, mqtt_password, mqtt_ssl_ca)

    @staticmethod
    def on_message(client, userdata, msg):
        """
        Defines action what to do if event receives
        """

        Subscriber.on_message(client, userdata, msg)

        logging.info((msg.topic + " " + str(msg.payload)))

        from config.Configuration import Configuration
        config = Configuration()

        influxdb_client = InfluxDbClient(config.read_config("influxdb", "host"),
                                         config.read_config("influxdb", "port"),
                                         config.read_config("influxdb", "username"),
                                         config.read_config("influxdb", "password"),
                                         config.read_config("influxdb", "database"))

        influxdb_client.write_entry("postbox", {"value": msg.payload, "topic": msg.topic})