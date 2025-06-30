#UI for the to-do web app

# streamlit_ui.py

import streamlit as st
import sqlite3
from logic import add_task, check, finish, undo_task, remove_task
from db_create import check_lists, create_list, delete_list

def get_connection():
    return sqlite3.connect('to_do_list.db')

def list_title(lst):
    col1, col2 = st.columns([0.9,0.2], vertical_alignment='bottom')
    with col1:
        st.title(f'{lst}')
    with col2:
        if st.button('Delete List', type='primary'):
            conn = get_connection()
            delete_list(lst)
            conn.commit()
            conn.close()
            st.rerun()

def no_list():
    st.warning('You currently have no lists')
    st.error('Please use the sidebar to create a list')

def create_task(lst):
    with st.form('Add a task', clear_on_submit=True):
        new_task = st.text_input('Enter yout task...', placeholder='task')
        submitted = st.form_submit_button('Add Task')
        if submitted and new_task.strip():
            try:
                conn = get_connection()
                add_task(conn, new_task.strip(), lst)
                conn.commit()
                conn.close()
                st.success(f'Task added: {new_task.strip()}')
            except ValueError:
                st.error('You cannot add two of the same tasks :(')

def show_tasks(lst):
    st.markdown('### Tasks')
    conn = get_connection()
    tasks = check(conn, lst)
    conn.close()
    if tasks:
        for task_id, emoji, task in tasks:
            col1, col2, col3 = st.columns([0.1,0.99,0.1], vertical_alignment='center')
            with col1:
                if st.button(emoji, key=f'btn_{task_id}'):
                    conn = get_connection()
                    if emoji == '✅':
                        undo_task(conn, task, lst, task_id)
                        conn.commit()
                        conn.close()
                        st.rerun()
                    elif emoji == '❌':
                        finish(conn, task, lst, task_id)
                        conn.commit()
                        conn.close()
                        st.rerun()
            with col2:
                st.text(f'{task}')
            with col3:
                if st.button('🗑️', key=f'dlt_{task_id}'):
                    conn = get_connection()
                    remove_task(conn, task, lst, task_id)
                    conn.commit()
                    conn.close()
                    st.rerun()
    else:
        st.info('No tasks yet!')


def task_page(lst):
    if lst:
        list_title(lst)
        create_task(lst)
        show_tasks(lst)
    else:
        no_list()
    
def new_list():
    st.header('Create a new list')
    with st.form('Create a new list', clear_on_submit=True):
        new_list = st.text_input('Name your list', placeholder='name')
        submitted = st.form_submit_button('Create list')
        if submitted and new_list.strip():
            try:
                create_list(new_list.strip())
                st.success(f'Created new list: {new_list}')
            except:
                st.error('Please use a new name')
            
def sidebar():
    with st.sidebar.form('Create a new list', clear_on_submit=True, enter_to_submit=False):
        new_list = st.text_input('Name your list', placeholder='name')
        submitted = st.form_submit_button('Create list')
        if submitted and new_list.strip():
                    try:
                        conn = get_connection()
                        conn.close()
                        create_list(new_list.strip())
                        st.success(f'Created new list: {new_list}',width='stretch')
                    except:
                        st.error('Please use a new name')


def get_lists():
    return [x[0] for x in check_lists() if x[0] != 'sqlite_sequence']


def main():
    sidebar()
    if not get_lists():
        no_list()
    else:
        demo_page = st.sidebar.selectbox('Checkout your lists', get_lists())
        task_page(demo_page)

if __name__ == "__main__":
    main()