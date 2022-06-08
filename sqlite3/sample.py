import sqlite3

database = 'sample.db'
connection = sqlite3.connect(database)
connection.close()
