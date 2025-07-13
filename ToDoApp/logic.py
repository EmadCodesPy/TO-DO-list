#Adding logic
def add_task(conn, task, lst, username):
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    c.execute('SELECT id FROM lists WHERE name=? AND username=?', (lst, username))
    result = c.fetchone()
    #if not result:
       #raise ValueError('List not found')
    list_id = result[0]
    c.execute(f"INSERT INTO tasks (emoji, task, list_id) VALUES (?,?,?) ", ('❌', task, list_id))
    conn.commit()
    conn.close()

#Checking logic
def check(conn, lst, username):
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    c.execute('SELECT id FROM lists WHERE name=? AND username=?', (lst, username))
    result = c.fetchone()
    #if not result:
        #raise ValueError('No tasks')
    list_id = result[0]
    c.execute("SELECT id,emoji,task FROM tasks WHERE list_id=?", (list_id,))
    return c.fetchall()


#Finishing logic
def finish(conn, lst, taskid, username):
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    c.execute('SELECT id FROM lists WHERE name=? AND username=?', (lst, username))
    result = c.fetchone()
    #if not result:
        #raise ValueError('No tasks')
    list_id = result[0]
    c.execute("UPDATE tasks SET emoji=? WHERE emoji=? AND id=? AND list_id=?", ('✅','❌', taskid, list_id))
    conn.commit()
    conn.close()

#Removing logic
def remove_task(conn, lst, taskid, username):
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    c.execute('SELECT id FROM lists WHERE name=? AND username=?', (lst, username))
    result = c.fetchone()
    #if not result:
        #raise ValueError('No tasks')
    list_id = result[0]
    c.execute("DELETE FROM tasks WHERE id=? AND list_id=?", (taskid, list_id))
    conn.commit()
    conn.close()

#Undoing logic
def undo_task(conn, lst, taskid, username):
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    c.execute('SELECT id FROM lists WHERE name=? AND username=?', (lst, username))
    result = c.fetchone()
    #if not result:
        #raise ValueError('No tasks')
    list_id = result[0]
    c.execute("UPDATE tasks SET emoji=? WHERE emoji=? AND id=? AND list_id=?", ('❌','✅',taskid, list_id))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    check()