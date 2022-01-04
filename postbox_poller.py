"""
check for events and publish them to mqtt
"""
import logging
import threading
import time

from config.configuration import Configuration
from mqtt.publisher import Publisher
from rf.client import RfClient

HAS_SIGNAL = False


def publish_signal():
    global HAS_SIGNAL

    threading.Timer(60, publish_signal).start()

    if HAS_SIGNAL:
        HAS_SIGNAL = False
        event_handler.publish("postbox_open")
        logging.info("Published event to queue")


publish_signal()

logging.basicConfig(filename='postbox.log', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

config = Configuration()

rf_client = RfClient(config.read_config("rf", "pin"))
event_handler = Publisher(str(config.read_config("mqtt", "host")),
                          int(config.read_config("mqtt", "port")),
                          str(config.read_config("mqtt", "topic")),
                          str(config.read_config("mqtt", "user")),
                          str(config.read_config("mqtt", "password")),
                          str(config.read_config("mqtt", "ssl_ca")))

while True:
    result = rf_client.read()
    if result is not None:
        logging.info("Received event %s", result)
        if config.read_config("rf", "filter") is None or result == int(config.read_config("rf", "filter")):
            HAS_SIGNAL = True
    time.sleep(1)  # wait one second until next check
