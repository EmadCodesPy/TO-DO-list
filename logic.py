#Adding logic
def add_task(conn, task):
    c = conn.cursor()
    c.execute(f"INSERT INTO 'do_list' VALUES (?,?) ", ('❌', task))

#Checking logic
def check(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM do_list")
    return c.fetchall() 

#Finishing logic
def finish(conn, task):
    c = conn.cursor()
    c.execute("UPDATE 'do_list' SET finished=? WHERE finished=? AND task=?", ('✅','❌', task))

#Removing logic
def remove_task(conn, task):
    c = conn.cursor()
    c.execute("DELETE FROM 'do_list' WHERE (finished=? OR finished =?) AND task=?", ('❌','✅',task))

#Undoing logic
def undo_task(conn, task):
    c = conn.cursor()
    c.execute("UPDATE 'do_list' SET finished=? WHERE finished=? AND task=?", ('❌','✅', task))
