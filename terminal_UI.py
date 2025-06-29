#a to-do list
#features include: General select, Adding a to-do, Checking the list, 
#Finishing a to-do, Deleting a to-do, Create a to-do list
import sqlite3
from logic import add_task, check, finish, remove_task, undo_task
from db_create import create_list, delete_list, check_lists
#c.execute(""" CREATE TABLE do_list (
 #           finished TEXT,
  #          task TEXT
   #     )
    #""")

#Adding a task
def adding_inp(lst):
    conn = sqlite3.connect('to_do_list.db')
    #loop for adding task multiple times
    while True:
        task = input('What task would you like to add? (Leave empty to stop adding): ')
        if task == '':
            break
        add_task(conn, task, lst)
    conn.commit()
    conn.close()

#Checking tasks
def check_inp(lst):
    conn = sqlite3.connect('to_do_list.db')
    tasks = check(conn, lst)
    for emoji, task in tasks:
        print(f"{emoji} {task}")
    conn.close()

#Finishing tasks
def finish_inp(lst):
    conn = sqlite3.connect('to_do_list.db')
    while True:
        task = input('What tasks have you finished? (Leave empty to stop changing status): ')
        if task == '':
            break
        finish(conn, task, lst)
        print ('✅ ' + task)
    conn.commit()
    conn.close()

#Removing a task
def remove_inp(lst):
    conn = sqlite3.connect('to_do_list.db')
    while True:
        task = input('What tasks would you like to remove? (Leave empty to stop removing): ')
        if task == '':
            break
        remove_task(conn, task, lst)
        print('REMOVED TASK: ' + task)
    conn.commit()
    conn.close()

#Undoing a task
def undo_inp(lst):
    conn = sqlite3.connect('to_do_list.db')
    while True:
        task = input('What task would you like to undo? (Leave empty to stop undoing): ')
        if task == '':
            break
        undo_task(conn, task, lst)
        conn.commit()
        conn.close()

#Adding a to-do list
def list_inp():
    conn = sqlite3.connect('to_do_list.db')
    while True:
        lst = input('What is the name of the list you would like to add: ')
        if lst == '':
            break
        create_list(lst)
        conn.commit()
        conn.close()

#Removing a to-do list
def r_list_inp():
    conn = sqlite3.connect('to_do_list.db')
    while True:
        lst = input('What is the name of the list you would like to remove: ')
        if lst == '':
            break
        delete_list(lst)
        conn.commit()
        conn.close()

#Checking all lists
def c_lists_inp():
    my_data = check_lists()
    for i in my_data:
        print(i)

#Select your function
def main():
    func = input('What would you like to do. Add(A), Check(C), Finish(F), Remove a task(R), Undo(U), Add a list(L), Delete a list(D), Check lists(CL): ')
    if func.upper() == 'A':
        lst = input("What list would you like to access: ")
        adding_inp(lst)
    elif func.upper() == 'C':
        lst = input("What list would you like to access: ")
        check_inp(lst)
    elif func.upper() == 'F':
        lst = input("What list would you like to access: ")
        finish_inp(lst)
    elif func.upper() == 'R':
        lst = input("What list would you like to access: ")
        remove_inp(lst)
    elif func.upper() == 'U':
        lst = input("What list would you like to access: ")
        undo_inp(lst)
    elif func.upper() == 'L':
        list_inp()
    elif func.upper() == 'D':
        r_list_inp()
    elif func.upper() == 'CL':
        c_lists_inp()

main()