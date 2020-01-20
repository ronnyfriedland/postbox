from config.Configuration import Configuration
from mqtt.publisher import Publisher
from rf.client import RfClient

import logging
import time

logging.basicConfig(filename='postbox.log', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

config = Configuration()

rf_client = RfClient(config.read_config("rf", "pin"))
event_handler = Publisher(config.read_config("mqtt", "host"),
                          config.read_config("mqtt", "port"),
                          config.read_config("mqtt", "topic"),
                          config.read_config("mqtt", "user"),
                          config.read_config("mqtt", "password"),
                          config.read_config("mqtt", "ssl_ca"))

while True:
    result = rf_client.read()
    if result is not None:
        logging.info("Received event '%s'" % result)
        if config.read_config("rf", "filter") is None or result == config.read_config("rf", "filter"):
            logging.info("Publish result '%s' to queue" % result)
            event_handler.publish("postbox_open")
    time.sleep(1)  # wait one second until next check
