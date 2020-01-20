from config.Configuration import Configuration
import logging

from influx_db.subscriber import InfluxDBSubscriber

logging.basicConfig(filename='postbox_influxdb.log', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

config = Configuration()

event_handler = InfluxDBSubscriber(config.read_config("mqtt", "host"),
                           config.read_config("mqtt", "port"),
                           config.read_config("mqtt", "topic"),
                           config.read_config("mqtt", "user"),
                           config.read_config("mqtt", "password"),
                           config.read_config("mqtt", "ssl_ca"))

event_handler.subscribe()
