import sqlite3
from model import Item


def get_items_list() -> list[Item]:
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "select * from item"
    result = cursor.execute(query)
    item_list = []

    for row in result:
        item_list.append(Item(*row))

    connection.close()
    return item_list


def get_item_by_name(name) -> Item:
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "select * from item where name=?"
    result = cursor.execute(query, (name,))
    row = result.fetchone()
    if row:
        item = Item(*row)
    else:
        item = None

    connection.close()
    return item


def persist_item(item):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "insert into item values (?,?)"
    cursor.execute(query, (item.name, item.price))

    connection.commit()
    connection.close()


def delete_item_by_name(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "delete from item where name=?"
    cursor.execute(query, (name,))

    connection.commit()
    connection.close()


def update_item(item):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "update item set price=? where name=?"
    cursor.execute(query, (item.price, item.name))

    connection.commit()
    connection.close()

