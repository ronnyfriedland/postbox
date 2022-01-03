"""
mqtt subsriber to send mails
"""
import smtplib
import sys
from email.message import EmailMessage

from mail.mailconfiguration import MailConfiguration
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

        # Subscriber.on_message(client, userdata, msg)
        config = MailConfiguration(vault=True)

        mail = EmailMessage()
        mail['Subject'] = "Sie haben Post ..."
        mail['From'] = config.read_config("mail", "sender")
        mail['To'] = config.read_config("mail", "recipient")
        mail.add_header('Content-Type', 'text/plain')
        mail.set_payload("Im Briefkasten wartet etwas auf dich !")

        server = None
        try:
            if config.read_config("mail", "ssl_ca") is not None:
                server = smtplib.SMTP_SSL(
                    host=str(config.read_config("mail", "host")),
                    port=int(config.read_config("mail", "port")),
                    certfile=str(config.read_config("mail", "ssl_ca")))
            else:

                server = smtplib.SMTP(
                    host=str(config.read_config("mail", "host")),
                    port=config.read_config("mail", "port"))
                server.starttls()

                server.ehlo()
                server.login(str(config.read_config("mail", "username")), str(config.read_config("mail", "password")))
                server.send_message(mail)
        except:
            print("Error!", sys.exc_info()[0], "occurred.")
        finally:
            if server is not None:
                server.quit()
