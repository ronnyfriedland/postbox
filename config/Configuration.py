from configparser import ConfigParser


class Configuration:
    """
    Author: Ronny Friedland

    Handles common configuration access
    """

    config_file = 'config.ini'

    def __init__(self, config_file=config_file, vault=False):
        self.config_file = config_file
        self.config = ConfigParser()
        self.config.read(self.config_file)

        if vault:
           import hvac, os

           client = hvac.Client(
               url=os.environ['VAULT_URL'],
               token=os.environ['VAULT_TOKEN'],
               verify=False)  # TODO: fixme
           print(self.config)
           self.config['mail']['host'] = client.secrets.kv.v1.read_secret(mount_point="website", path="mailserver_host")["data"]["value"]
           self.config['mail']['port'] = client.secrets.kv.v1.read_secret(mount_point="website", path="mailserver_port")["data"]["value"]
           self.config['mail']['username'] = client.secrets.kv.v1.read_secret(mount_point="website", path="mailserver_username")["data"]["value"]
           self.config['mail']['password'] = client.secrets.kv.v1.read_secret(mount_point="website", path="mailserver_password")["data"]["value"]
           self.config['mail']['sender'] = client.secrets.kv.v1.read_secret(mount_point="website", path="mailserver_sender")["data"]["value"]
           self.config['mail']['recipient'] = client.secrets.kv.v1.read_secret(mount_point="website", path="mailserver_recipient")["data"]["value"]


    def check_config(self, section):
        """
        Check if config.ini contains given section
        :param section: section to check
        :return: true if configuration contains section
        """
        return self.config.has_section(section)

    def read_config(self, section, key):
        """
        Reads the configuration value for the given key
        :param section: the section to read
        :param key: the key to evaluate
        :return: the stored value for the given key
        """
        return self.config.get(section, key, fallback=None)
