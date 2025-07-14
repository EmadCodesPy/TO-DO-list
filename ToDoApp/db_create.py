#run once to create the databse
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(BASE_DIR, 'to_do_list.db')




def create_list(l_name, username):
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.execute('PRAGMA foreign_keys = ON')
    c = conn.cursor()
    c.execute('INSERT INTO lists (name, username) VALUES (?,?)', (l_name, username))
    conn.commit()
    conn.close()

def delete_list(l_name, username):
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.execute('PRAGMA foreign_keys = ON')
    c = conn.cursor()
    c.execute('SELECT id FROM lists WHERE name = ? AND username=?', (l_name, username))
    row = c.fetchone()
    if row:
        list_id = row[0]
        c.execute("DELETE FROM tasks WHERE list_id = ?", (list_id,))
        c.execute("DELETE FROM lists WHERE id = ?", (list_id,))
    conn.commit()
    conn.close()
    
def check_lists(username):
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.execute('PRAGMA foreign_keys = ON')
    c = conn.cursor()
    c.execute("SELECT name FROM lists WHERE username=?", (username,))
    my_lists = [x for x in c.fetchall()]
    return my_lists

