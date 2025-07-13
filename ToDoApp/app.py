#UI for the to-do web app

# streamlit_ui.py

import streamlit as st
import sqlite3
from logic import add_task, check, finish, undo_task, remove_task
from db_create import check_lists, create_list, delete_list
import os
from login import Login, Sign_Up
from utils import get_username, remove_user

def get_connection():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'to_do_list.db')
    return sqlite3.connect(db_path, check_same_thread=False)

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
    
def add_list():
    list_name = st.text_input('List Name', placeholder='...', )
    submit = st.button('➕ Create list')
    if list_name.strip() and submit:
        try:
            conn = get_connection()
            conn.close()
            create_list(list_name.strip())
            st.success(f'Created new list: {list_name}',width='stretch')
        except:
            st.error('Please use a new name')

def get_lists():
    return [x[0] for x in check_lists() if x[0] != 'sqlite_sequence']

def log_in_page():
    pg = st.navigation([Login, Sign_Up], position='top')
    pg.run()

def logout():
    if st.sidebar.button('🔓 Logout'):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.name = None
        st.rerun()

def check_list_exists():
    if not get_lists():
        no_list()
    else:
        demo_page = st.sidebar.selectbox('Checkout your lists', get_lists())
        task_page(demo_page)

def username_display():
    st.sidebar.text(f'You are signed in as {get_username(st.session_state.username)}')

def remove_account():
    if 'delete_flow_active' not in st.session_state:
        st.session_state.delete_flow_active = False
    if not st.session_state.delete_flow_active:
        if st.sidebar.button('Delete Account', type='primary', icon='🗑️'):
            st.session_state.delete_flow_active = True
            st.rerun()
    else:
        st.sidebar.warning('This will :red[Permanently] delete your account')
        st.sidebar.text_input('Type YES to delete', key='confirm_delete_input')
        col1, col2 = st.columns([1,1])
        with col1:
            if st.button('', icon='🗑️', type='primary'):
                if st.session_state.confirm_delete_input.strip() == 'YES':
                    remove_user(get_username(st.session_state.username))
                    st.success('Account Deleted')
                    st.session_state.logged_in = False
                    st.session_state.username = None
                    st.session_state.name = None
                    st.session_state.delete_flow_active = False
                    st.rerun()
                else:
                    st.toast('You must type YES to confirm')
        with col2:
            if st.button('Cancel'):
                st.session_state.delete_flow_active = False
                st.rerun()


def sidebar():
    with st.sidebar:
        st.markdown('### 👤 Account')
        st.markdown(f'**You are signed in as** {get_username(st.session_state.username)}')
        logout()
        remove_account()

        st.markdown('---')
        st.markdown('### 📋 Create a New List')

        add_list()


def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.name = None
    pg = st.navigation([st.Page('login.py', title='Emad\'s to-do web app')], position='top')
    if not st.session_state.logged_in:
        pg.run()
    elif st.session_state.logged_in:
        sidebar()
        check_list_exists()

if __name__ == "__main__":
    main()