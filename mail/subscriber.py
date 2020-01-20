import logging, smtplib, ssl

from mqtt.subscriber import Subscriber


class MailSubscriber(Subscriber):
    def __init__(self, mqtt_host, mqtt_port, mqtt_topic, mqtt_user, mqtt_password, mqtt_ssl_ca):
        """
        Initializes the mail subscriber instance
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

        super().on_message(client, userdata, msg)

        logging.info((msg.topic + " " + str(msg.payload)))

        from config.Configuration import Configuration
        config = Configuration()

        server = smtplib.SMTP_SSL(host=config.read_config("mail", "host"), port=config.read_config("mail", "port"), certfile=config.read_config("mail", "ssl_ca"))
        try:
            server.ehlo()
            server.login(config.read_config("mail", "username"), config.read_config("mail", "password"))
            server.send_message(msg, config.read_config("mail", "sender"), config.read_config("mail", "recipient"))
        finally:
            server.quit()

