#UI for the to-do web app

# streamlit_ui.py

import streamlit as st
import sqlite3
from logic import add_task, check, finish, undo_task, remove_task
from time import sleep

def get_connection():
    return sqlite3.connect('/Users/Emad/Desktop/Github port/to-do/to-do-list.db')

st.title('To-Do List')

with st.form('Add a task', clear_on_submit=True):
    new_task = st.text_input('Enter yout task...', placeholder='task')
    submitted = st.form_submit_button('Add Task')
    if submitted and new_task.strip():
        try:
            conn = get_connection()
            add_task(conn, new_task.strip())
            conn.commit()
            conn.close()
            st.success(f'Task added: {new_task.strip()}')
        except ValueError as e:
            st.error('You cannot add two of the same tasks :(')
    


st.markdown('### Tasks')
conn = get_connection()
tasks = check(conn)
conn.close()

if tasks:
    for emoji, task in tasks:
        col1, col2, col3 = st.columns([0.1,0.99,0.1], vertical_alignment='center')
        with col1:
            if st.button(emoji, key=f'btn_{task}'):
                conn = get_connection()
                if emoji == '✅':
                    undo_task(conn, task)
                    conn.commit()
                    conn.close()
                    st.rerun()
                elif emoji == '❌':
                    finish(conn, task)
                    conn.commit()
                    conn.close()
                    st.rerun()
        with col2:
            st.text(f'{task}')
        with col3:
            if st.button('🗑️', key=f'dlt_{task}'):
                conn = get_connection()
                remove_task(conn, task)
                conn.commit()
                conn.close()
                st.rerun()
else:
    st.info('No tasks yet!')


