#a to-do list
#features include: General select, Adding a to-do, Checking the list, 
#Finishing a to-do, Deleting a to-do
import sqlite3
from logic import add_task, check, finish, remove_task, undo_task

#c.execute(""" CREATE TABLE do_list (
 #           finished TEXT,
  #          task TEXT
   #     )
    #""")

#Adding a task
def adding_inp():
    conn = sqlite3.connect('/Users/Emad/Desktop/Github port/to-do/to-do-list.db')
    #loop for adding task multiple times
    while True:
        task = input('What task would you like to add? (Leave empty to stop adding): ')
        if task == '':
            break
        add_task(conn, task)
    conn.commit()
    conn.close()

#Checking tasks
def check_inp():
    conn = sqlite3.connect('/Users/Emad/Desktop/Github port/to-do/to-do-list.db')
    tasks = check(conn)
    for emoji, task in tasks:
        print(f"{emoji} {task}")
    conn.close()

#Finishing tasks
def finish_inp():
    conn = sqlite3.connect('/Users/Emad/Desktop/Github port/to-do/to-do-list.db')
    while True:
        task = input('What tasks have you finished? (Leave empty to stop changing status): ')
        if task == '':
            break
        finish(conn, task)
        print ('✅ ' + task)
    conn.commit()
    conn.close()

#Removing a task
def remove_inp():
    conn = sqlite3.connect('/Users/Emad/Desktop/Github port/to-do/to-do-list.db')
    while True:
        task = input('What tasks would you like to remove? (Leave empty to stop removing): ')
        if task == '':
            break
        remove_task(conn, task)
        print('REMOVED TASK: ' + task)
    conn.commit()
    conn.close()

#Undoing a task
def undo_inp():
    conn = sqlite3.connect('/Users/Emad/Desktop/Github port/to-do/to-do-list.db')
    while True:
        task = input('What task would you like to undo? (Leave empty to stop undoing): ')
        if task == '':
            break
        undo_task(conn, task)
        conn.commit()
        conn.close()

#Select your function
func = input('What would you like to do. Add a task(A), Check your tasks(C), Finish a task(F), Remove a task(R), Undo a task(U): ')
if func.upper() == 'A':
    adding_inp()
elif func.upper() == 'C':
    check_inp()
elif func.upper() == 'F':
    finish_inp()
elif func.upper() == 'R':
    remove_inp()
elif func.upper() == 'U':
    undo_inp()