import bcrypt
import sqlite3

conn = sqlite3.connect("to_do_list.db", check_same_thread=False)
c = conn.cursor()

def create_user_db():
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
def user_exists(username):
    c.execute(f'SELECT * FROM users WHERE username=?', (username,))
    return c.fetchone() is not None

#Validates login
def login_user(username, password, connection):
    c = connection.cursor()
    c.execute(f'SELECT password FROM users WHERE username=?', (username,))
    row = c.fetchone()
    if row:
        return bcrypt.checkpw(password.encode(), row[0].encode())
    return False

#below is for testing
def remove_user(username):
    c.execute('DELETE FROM users WHERE username=?', (username,))
    conn.commit()

def get_username(username):
    c.execute('SELECT username FROM users WHERE username=?', (username,))
    return c.fetchone()[0]

#if __name__ == '__main__':
