import sqlite3


def select(table, column, filter_column, filter_value):
    '''Makes a query to the database. Parameters will be sanitized before being sent to the db'''

    conn = sqlite3.connect('db.db')
    c = conn.cursor()

    c.execute('SELECT ? FROM ? WHERE ? = ?', (column, table, filter_column, filter_value))
    res = c.fetchall()

    conn.close()
    return res

def update(table, id, column, value):
    conn = sqlite3.connect('db.db')
    c = conn.cursor()

    c.execute('UPDATE ? SET ? = ? WHERE id = ?', (table, column, value, id))

    conn.close()

def insert(table, id,)