import sqlite3
from sqlite3 import Connection

DEFAULT_DATABASE = 'sample.db'


def connect_to_database(database: str = DEFAULT_DATABASE) -> Connection:
    connection = sqlite3.connect(database)
    return connection


def close_database(connection: Connection) -> None:
    connection.close()
