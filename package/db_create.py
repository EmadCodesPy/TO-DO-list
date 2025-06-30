#run once to create the databse
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(BASE_DIR, 'to_do_list.db')

conn = sqlite3.connect(db_path, check_same_thread=False)
c = conn.cursor()


def create_list(l_name):
    c.execute(f""" CREATE TABLE '{l_name}' (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                emoji TEXT,
                task TEXT
            )
        """)

def delete_list(l_name):
    c.execute(f"DROP TABLE IF EXISTS '{l_name}'")
    
def check_lists():
    c.execute(f"""SELECT name FROM sqlite_master WHERE type='table';""")
    my_lists = [x for x in c.fetchall()]
    return my_lists