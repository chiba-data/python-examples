from sqlite3 import Connection

from cdcc.sample.sqlite3.sample import connect_to_database, close_database, create_table, drop_table, insert_into, \
    select_all

DATABASE = ':memory:'


def test_connect_to_database():
    try:
        connection = connect_to_database(DATABASE)
        assert isinstance(connection, Connection)
    except ConnectionError \
           or ConnectionResetError \
           or ConnectionAbortedError \
           or ConnectionRefusedError:  # pragma no cover
        assert False


def test_close_database():
    try:
        connection = connect_to_database(DATABASE)
        close_database(connection)
        assert True
    except ConnectionError \
           or ConnectionResetError \
           or ConnectionRefusedError \
           or ConnectionAbortedError:  # pragma no cover
        assert False


def test_create_and_drop_table():
    connection = connect_to_database(DATABASE)
    cursor = connection.cursor()
    create_table(cursor)
    drop_table(cursor)
    close_database(connection)


def test_insert_and_select():
    connection = connect_to_database(DATABASE)
    cursor = connection.cursor()
    create_table(cursor)
    insert_into(cursor, [
        ('1001-01', '建設業4月分'),
        ('1002', '共済定例4月分'),
        ('1003-02', '減免申請書4月分')
    ])
    select_all(cursor)

    assert len(cursor.fetchall()) == 3
