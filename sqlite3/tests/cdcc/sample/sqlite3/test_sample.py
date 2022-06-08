from sqlite3 import Connection

from cdcc.sample.sqlite3.sample import connect_to_database, close_database, create_table, drop_table

DATABASE = ':memory:'


def test_connect_to_database():
    try:
        connection = connect_to_database(DATABASE)
        assert isinstance(connection, Connection)
    except ConnectionError \
           or ConnectionResetError \
           or ConnectionAbortedError \
           or ConnectionRefusedError:
        assert False


def test_close_database():
    try:
        connection = connect_to_database(DATABASE)
        close_database(connection)
        assert True
    except ConnectionError \
           or ConnectionResetError \
           or ConnectionRefusedError \
           or ConnectionAbortedError:
        assert False


def test_create_and_drop_table():
    connection = connect_to_database(DATABASE)
    cursor = connection.cursor()
    create_table(cursor)
    drop_table(cursor)
    close_database(connection)
