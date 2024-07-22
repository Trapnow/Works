import sqlite3 as sq

from aiogram.fsm.state import StatesGroup, State


class NewOrder(StatesGroup):
    name = State()
    type = State()
    num_one = State()
    background = State()
    phone = State()


db = sq.connect("tg1.db")
cur = db.cursor()


async def db_start():
    cur.execute('CREATE TABLE IF NOT EXISTS orders('
                'id INTEGER  PRIMARY KEY AUTOINCREMENT,'
                'name TEXT,'
                'type TEXT,'
                'num_one INTEGER,'
                'background TEXT,'
                'phone TEXT)'
                )
    db.commit()


async def add_order(data):
    cur.execute('INSERT INTO orders (name, type, num_one, background, phone) VALUES (?, ?, ?, ?, ?)',
                (data['name'], data['type'], data['num_one'], data['background'], data['phone']))
    db.commit()
