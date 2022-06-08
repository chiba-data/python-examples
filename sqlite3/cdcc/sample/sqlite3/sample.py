import sqlite3
from sqlite3 import Connection

DEFAULT_DATABASE = 'sample.db'


def connect_to_database(database: str = DEFAULT_DATABASE) -> Connection:
    """データベース接続オブジェクトを返却する。

    :param database: データベースファイル名(省略時:'sample.db')
    :return: データベース接続オブジェクト
    :rtype: Connection
    """
    connection = sqlite3.connect(database)
    return connection


def close_database(connection: Connection) -> None:
    """データベース接続を閉じる。

    :param Connection connection: データベース接続オブジェクト
    :return: なし
    :rtype: None
    """
    connection.close()
