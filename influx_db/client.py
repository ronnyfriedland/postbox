import datetime

from influxdb import InfluxDBClient


class InfluxDbClient:

    """
    Author: Ronny Friedland

    Encapsulates influxdb access
    """

    def __init__(self, host, port, username, password, database):
        """
        Initializes the subscriber instance

        :param host: the influxdb host
        :param port: the influxdb port
        :param username: the influxdb username
        :param password: the influxdb password
        :param database: the influxdb database
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

    def write_entry(self, measurement, data):
        """
        Writes a new entry to the influxdb
        :param measurement: name of the measurement
        :param data: the data to write
        """
        entry = [
            {
                "measurement": measurement,
                "time": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M'),
                "fields": data
            }
        ]
        connection = InfluxDBClient(self.host, int(self.port), self.username, self.password, self.database)
        try:
            connection.write_points(entry, time_precision="u")
        finally:
            connection.close()
