import sqlite3

from model import User


def find_by_username(username) -> User:
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "select * from user where username=?"
    result = cursor.execute(query, (username,))
    row = result.fetchone()
    if row:
        # user = User(row[0], row[1], row[2])
        user = User(*row)
    else:
        user = None

    connection.close()
    return user


def find_by_id(id) -> User:
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "select * from user where id=?"
    result = cursor.execute(query, (id,))
    row = result.fetchone()
    if row:
        # user = User(row[0], row[1], row[2])
        user = User(*row)
    else:
        user = None

    connection.close()
    return user


def persist_user(data):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "insert into user values (NULL ,?,?)"
    cursor.execute(query, (data['username'], data['password']))

    connection.commit()
    connection.close()
