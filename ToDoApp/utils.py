import bcrypt
import sqlite3

#conn = sqlite3.connect("to_do_list.db", check_same_thread=False)
#c = conn.cursor()

def create_user_db():
    conn = sqlite3.connect("to_do_list.db", check_same_thread=False)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
              username TEXT PRIMARY KEY,
              name TEXT,
              password TEXT
        )
    ''')
    conn.commit()

#adding a new user
def add_user(username, name, password,conn):
    c = conn.cursor()
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    c.execute(f'INSERT INTO users (username, name, password) VALUES (?,?,?)', (username, name, hashed_pw))
    conn.commit()

#Checks if user exists
def user_exists(username, conn):
    c = conn.cursor()
    c.execute(f'SELECT * FROM users WHERE username=?', (username,))
    return c.fetchone() is not None

#Validates login
def login_user(username, password, conn):
    c = conn.cursor()
    c.execute(f'SELECT password FROM users WHERE username=?', (username,))
    row = c.fetchone()
    if row:
        return bcrypt.checkpw(password.encode(), row[0].encode())
    return False

#below is for testing
def remove_user(username, conn):
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE username=?', (username,))
    conn.commit()
    conn.close()

def get_username(username, conn):
    c = conn.cursor()
    c.execute('SELECT username FROM users WHERE username=?', (username,))
    return c.fetchone()[0]

#if __name__ == '__main__':
