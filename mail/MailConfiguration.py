"""
mail related configuration
"""
import os

import hvac

from config.configuration import Configuration


class MailConfiguration(Configuration):
    """
    Author: Ronny Friedland

    Handles mail configuration access
    Allows reading configuration from vault
    """

    vault_mount = 'postbox'

    def __init__(self, vault=False, vault_mount=vault_mount):
        super().__init__()

        if vault:
            client = hvac.Client(
                url=os.environ['VAULT_URL'],
                token=os.environ['VAULT_TOKEN'],
                verify=False)  # TODO: fixme
            print(self.config)
            self.config['mail']['host'] = \
                client.secrets.kv.v2.read_secret(mount_point=vault_mount, path="mailserver_host")["data"]["data"][
                    "value"]
            self.config['mail']['port'] = \
                client.secrets.kv.v2.read_secret(mount_point=vault_mount, path="mailserver_port")["data"]["data"][
                    "value"]
            self.config['mail']['username'] = \
                client.secrets.kv.v2.read_secret(mount_point=vault_mount, path="mailserver_username")["data"]["data"][
                    "value"]
            self.config['mail']['password'] = \
                client.secrets.kv.v2.read_secret(mount_point=vault_mount, path="mailserver_password")["data"]["data"][
                    "value"]
            self.config['mail']['sender'] = \
                client.secrets.kv.v2.read_secret(mount_point=vault_mount, path="mailserver_sender")["data"]["data"][
                    "value"]
            self.config['mail']['recipient'] = \
                client.secrets.kv.v2.read_secret(mount_point=vault_mount, path="mailserver_recipient")["data"]["data"][
                    "value"]
