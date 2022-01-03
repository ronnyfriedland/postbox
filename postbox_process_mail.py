"""
process mqtt message and send e-mail
"""
import logging

from config.configuration import Configuration
from mail.subscriber import MailSubscriber

logging.basicConfig(filename='postbox_mail.log', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

config = Configuration()

event_handler = MailSubscriber(
    str(config.read_config("mqtt", "host")),
    int(config.read_config("mqtt", "port")),
    str(config.read_config("mqtt", "topic")),
    str(config.read_config("mqtt", "user")),
    str(config.read_config("mqtt", "password")),
    str(config.read_config("mqtt", "ssl_ca")))

event_handler.subscribe()
