import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table_user = "create table if not exists user(id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table_user)

create_table_item = "create table if not exists item (name text, price real)"
cursor.execute(create_table_item)

cursor.execute("insert into item values ('test', 10.99)")
connection.commit()

# users = [
#     (1, 'jose', 'asdf'),
#     (2, 'rolf', 'asdf'),
#     (3, 'anne', 'asdf')
# ]
#
# insert_query = "insert into user values (?, ?, ?)"
# cursor.executemany(insert_query, users)
# connection.commit()

connection.close()
