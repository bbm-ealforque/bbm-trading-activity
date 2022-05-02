"""Task Module Description"""
from masonite.scheduling import Task
from masonite.environment import env

from paramiko import RSAKey
from sshtunnel import SSHTunnelForwarder

class EstablishSSHTunnelTask(Task):
    def handle(self):
        try:
            server = SSHTunnelForwarder((
                    env("MYSQL_SSH_SERVER"), 
                    env("MYSQL_SSH_PORT")
                ),
                ssh_username = env("MYSQL_SSH_USER"),
                ssh_pkey = RSAKey.from_private_key_file(env("MYSQL_SSH_PEM_FILE")),
                remote_bind_address = (
                    env("MYSQL_HOST"), 
                    env("MYSQL_PORT")
                ),
                local_bind_address = (
                    "localhost", 
                    env("DB_PORT")
                ),
            )

            server.start()
        except:
            print("Error in establishing SSH tunnel")
        
