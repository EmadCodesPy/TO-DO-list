#run once to create the databse
import sqlite3

conn = sqlite3.connect('to_do_list.db')
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