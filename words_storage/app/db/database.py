import sqlite3
from flask import g

_DATABASE = 'words.db'

EXISTS_TABLE = (
    'words_en_ru',
)


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(_DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


def init_db():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words_en_ru (
            id INTEGER PRIMARY KEY,
            original TEXT NOT NULL,
            translation TEXT NOT NULL,
            meta TEXT
        )
    ''')
    db.commit()
