from sqlite3 import Connection

from cdcc.sample.sqlite3.sample import connect_to_database, close_database


def test_connect_to_database():
    try:
        connection = connect_to_database()
        assert isinstance(connection, Connection)
    except ConnectionError \
           or ConnectionResetError \
           or ConnectionAbortedError \
           or ConnectionRefusedError:
        assert False


def test_close_database():
    try:
        connection = connect_to_database()
        close_database(connection)
        assert True
    except ConnectionError \
           or ConnectionResetError \
           or ConnectionAbortedError \
           or ConnectionRefusedError:
        assert False
