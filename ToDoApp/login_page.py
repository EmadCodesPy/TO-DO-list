import streamlit as st
from utils import add_user, login_user, user_exists
import time
import os
import sqlite3

#create_user_db()

def get_connection():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(os.path.join(BASE_DIR, 'to_do_list.db'))
    conn.execute("PRAGMA foreign_keys = ON")
    return conn
def Login():
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    conn = get_connection()
    if st.button('Login'):
        if login_user(username, password, conn):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.name = username
            st.success('Logged in succesfully')
            time.sleep(1)
            st.rerun()
        elif username == '' or password == '':
            st.error('Please fill in a username and password')
        else:
            st.error('Invalid username or password')

def Sign_Up():
    st.title('Sign Up')
    username = st.text_input('Userrname')
    name = st.text_input('Full name')
    password = st.text_input('Password', type='password')
    conn = get_connection()
    if st.button('Create Account'):
        if user_exists(username, conn):
            st.error('Username already exists :(')
        else:
            add_user(username, name, password, conn)
            st.success('Account Created')
            time.sleep(1)

if __name__ == '__main__':
    pg = st.navigation([Login, Sign_Up], position='top')
    pg.run()