#Adding logic
def add_task(conn, task, lst):
    c = conn.cursor()
    c.execute(f"INSERT INTO '{lst}' (emoji, task) VALUES (?,?) ", ('❌', task))

#Checking logic
def check(conn, lst):
    c = conn.cursor()
    c.execute(f"SELECT * FROM {lst}")
    return c.fetchall() 

#Finishing logic
def finish(conn, task, lst):
    c = conn.cursor()
    c.execute(f"UPDATE '{lst}' SET emoji=? WHERE emoji=? AND task=?", ('✅','❌', task))

#Removing logic
def remove_task(conn, task, lst):
    c = conn.cursor()
    c.execute(f"DELETE FROM '{lst}' WHERE (emoji=? OR emoji =?) AND task=?", ('❌','✅',task))

#Undoing logic
def undo_task(conn, task, lst):
    c = conn.cursor()
    c.execute(f"UPDATE '{lst}' SET emoji=? WHERE emoji=? AND task=?", ('❌','✅', task))
