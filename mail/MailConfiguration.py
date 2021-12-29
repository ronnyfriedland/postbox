from config.Configuration import Configuration

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
           import hvac, os

           client = hvac.Client(
               url=os.environ['VAULT_URL'],
               token=os.environ['VAULT_TOKEN'],
               verify=False)  # TODO: fixme
           print(self.config)
           self.config['mail']['host'] = client.secrets.kv.v1.read_secret(mount_point=vault_mount, path="mailserver_host")["data"]["value"]
           self.config['mail']['port'] = client.secrets.kv.v1.read_secret(mount_point=vault_mount, path="mailserver_port")["data"]["value"]
           self.config['mail']['username'] = client.secrets.kv.v1.read_secret(mount_point=vault_mount, path="mailserver_username")["data"]["value"]
           self.config['mail']['password'] = client.secrets.kv.v1.read_secret(mount_point=vault_mount, path="mailserver_password")["data"]["value"]
           self.config['mail']['sender'] = client.secrets.kv.v1.read_secret(mount_point=vault_mount, path="mailserver_sender")["data"]["value"]
           self.config['mail']['recipient'] = client.secrets.kv.v1.read_secret(mount_point=vault_mount, path="mailserver_recipient")["data"]["value"]
