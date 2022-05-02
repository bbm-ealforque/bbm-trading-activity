import os
from masonite.environment import LoadEnvironment, env
from masoniteorm.connections import ConnectionResolver
from masonite.facades import Config
from masonite.configuration import config

from paramiko import RSAKey
from sshtunnel import SSHTunnelForwarder

#  Loads in the environment variables when this page is imported.
LoadEnvironment()

"""
The connections here don't determine the database but determine the "connection".
They can be named whatever you want.
"""
DATABASES = {
    "default": env("DB_CONNECTION", "mysql-mt4"),
    "mysql-mt4": {
        "driver": "mysql",
        "host": env("DB_MT4_HOST"),
        "user": env("DB_MT4_USERNAME"),
        "password": env("DB_MT4_PASSWORD"),
        "database": env("DB_MT4_DATABASE"),
        "port": env("DB_MT4_PORT"),
        "prefix": "",
        "grammar": "mysql",
        "options": {
            "charset": "utf8mb4",
        },
        "log_queries": env("DB_LOG"),
    },
    "mysql-mt5": {
        "driver": "mysql",
        "host": env("DB_MT5_HOST"),
        "user": env("DB_MT5_USERNAME"),
        "password": env("DB_MT5_PASSWORD"),
        "database": env("DB_MT5_DATABASE"),
        "port": env("DB_MT5_PORT"),
        "prefix": "",
        "grammar": "mysql",
        "options": {
            "charset": "utf8mb4",
        },
        "log_queries": env("DB_LOG"),
    },
}

LOCAL_BIND_PORTS = [ 3307, 3308, 3309, 3310, 3311, 3312 ]

for port in LOCAL_BIND_PORTS:
    try:
        SSHSERVER = SSHTunnelForwarder((
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
                port
            ),
        )
        print("Starting SSH tunnel on port: " + str(port))
        SSHSERVER.start()
    except:
        print("Error starting SSH tunnel on port: " + str(port))
    else:
        os.environ['DB_MT4_PORT'] = str(port)
        os.environ['DB_MT5_PORT'] = str(port)
        print("SSH tunnel started on port: " + str(port))
        break

DB = ConnectionResolver().set_connection_details(DATABASES)
