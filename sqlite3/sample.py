from cdcc.sample.sqlite3.sample import connect_to_database, create_table, insert_into

connection = connect_to_database()
cursor = connection.cursor()
create_table(cursor)
insert_into(cursor, [])
