#Adding logic
def add_task(conn, task):
    c = conn.cursor()
    c.execute(f"INSERT INTO 'do_list' VALUES (?,?) ", ('❌', task))

#Checking logic
def checking(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM do_list")
    return c.fetchall() 