import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(BASE_DIR, 'to_do_list.db')

#Adding logic
def add_task(task, lst, username):
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    c.execute('SELECT id FROM lists WHERE name=? AND username=?', (lst, username))
    result = c.fetchone()
    if result is None:
        raise TypeError(f'You had an error. Here {result, lst, username}')
    list_id = result[0]
    c.execute(f"INSERT INTO tasks (emoji, task, list_id) VALUES (?,?,?) ", ('❌', task, list_id))
    conn.commit()
    conn.close()

#Checking logic
def check(lst, username):
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    c.execute('SELECT id FROM lists WHERE name=? AND username=?', (lst, username))
    result = c.fetchone()
    if result is None:
        return None
    list_id = result[0]
    c.execute("SELECT id,emoji,task FROM tasks WHERE list_id=?", (list_id,))
    return c.fetchall()


#Finishing logic
def finish(lst, taskid, username):
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    c.execute('SELECT id FROM lists WHERE name=? AND username=?', (lst, username))
    result = c.fetchone()
    if result is None:
        return None
    list_id = result[0]
    c.execute("UPDATE tasks SET emoji=? WHERE emoji=? AND id=? AND list_id=?", ('✅','❌', taskid, list_id))
    conn.commit()
    conn.close()

#Removing logic
def remove_task(lst, taskid, username):
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    c.execute('SELECT id FROM lists WHERE name=? AND username=?', (lst, username))
    result = c.fetchone()
    if result is None:
        return None
    list_id = result[0]
    c.execute("DELETE FROM tasks WHERE id=? AND list_id=?", (taskid, list_id))
    conn.commit()
    conn.close()

#Undoing logic
def undo_task(lst, taskid, username):
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    c.execute('SELECT id FROM lists WHERE name=? AND username=?', (lst, username))
    result = c.fetchone()
    if result is None:
        return None
    list_id = result[0]
    c.execute("UPDATE tasks SET emoji=? WHERE emoji=? AND id=? AND list_id=?", ('❌','✅',taskid, list_id))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    check()