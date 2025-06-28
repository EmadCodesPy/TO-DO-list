#Adding logic
def add_task(conn, task):
    c = conn.cursor()
    c.execute(f"INSERT INTO 'do_list' VALUES (?,?) ", ('❌', task))