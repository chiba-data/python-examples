import sqlite3
from sqlite3 import Connection, Cursor

DEFAULT_DATABASE = 'sample.db'


def connect_to_database(database: str = DEFAULT_DATABASE) -> Connection:
    """データベース接続オブジェクトを返却する。

    :param database: データベースファイル名(省略時:'sample.db')
    :return: データベース接続オブジェクト
    :rtype: Connection
    """

    return sqlite3.connect(database)


def close_database(connection: Connection) -> None:
    """データベース接続を閉じる。

    :param Connection connection: データベース接続オブジェクト
    :return: なし
    :rtype: None
    """

    return connection.close()


def create_table(cursor: Cursor) -> Cursor:
    """job_noテーブルを作成し、Cursorオブジェクトを返却する。

    :param Cursor cursor: Cursorオブジェクト
    :return: Cursorオブジェクト
    :rtype: Cursor
    """

    sql = 'CREATE TABLE jobs(id INTEGER PRIMARY KEY AUTOINCREMENT, no STRING, name STRING)'
    return cursor.execute(sql)


def drop_table(cursor: Cursor) -> Cursor:
    """job_noテーブルを削除し、Cursorオブジェクトを返却する。

    :param Cursor cursor: Cursorオブジェクト
    :return: Cursorオブジェクト
    :rtype: Cursor
    """

    sql = 'DROP TABLE jobs'
    return cursor.execute(sql)


def insert_into(cursor: Cursor, new_data: [(str, str)]) -> Cursor:
    """新規データの投入

    :param Cursor cursor: Cursorオブジェクト
    :param list[tuple[str, str]] new_data: 投入するデータの配列 例:[('1003-02', '共済定例4月分'),('1004-02', '減免申請書5月分'),...]
    :return: Cursorオブジェクト
    :rtype: Cursor
    """

    return cursor.executemany('INSERT INTO jobs(no, name) values(?, ?)', new_data)


def select_all(cursor: Cursor) -> Cursor:
    """jobsテーブルからデータを全件取得し、返却する

    :param Cursor cursor: Cursorオブジェクト
    :return: Cursorオブジェクト
    :rtype: Cursor
    """

    sql = 'SELECT * FROM jobs'
    return cursor.execute(sql)
