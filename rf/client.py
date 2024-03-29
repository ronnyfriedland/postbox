"""
rf client to receive signals
"""
import logging
import signal

from rpi_rf import RFDevice


class RfClient:
    """
    Author: Ronny Friedland

    Provides methods to access the rf 433mhz client
    """
    timestamp = None

    def __init__(self, pin):
        """
        Constructor to initialize der receiver connected to the given pin
        :param pin:
        """
        self.rfdevice = RFDevice(int(pin))
        self.rfdevice.enable_rx()

        signal.signal(signal.SIGINT, self.cleanup)

    def cleanup(self):
        """
        If initialized cleanup
        :return:
        """
        if self.rfdevice is not None:
            self.rfdevice.cleanup()

    def read(self):
        """
        Reads the current available data
        :return: the transmitted code or None if no signal
        """
        if self.rfdevice.rx_code_timestamp != self.timestamp:
            self.timestamp = self.rfdevice.rx_code_timestamp
            logging.info("%s [pulselength=%s, protocol=%s]", str(self.rfdevice.rx_code),
                         str(self.rfdevice.rx_pulselength), str(self.rfdevice.rx_proto))
            return self.rfdevice.rx_code

        return None
