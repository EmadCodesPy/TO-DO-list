#a to-do list
#features include: General select, Adding a to-do, Checking the list, 
#Finishing a to-do, Deleting a to-do, Making a new list
import sqlite3

conn = sqlite3.connect('/Users/Emad/Desktop/Github port/to-do/to-do-list.db')
c = conn.cursor()

#c.execute(""" CREATE TABLE do_list (
 #           finished TEXT,
  #          task TEXT
   #     )
    #""")

#Adding a task
def adding():
    def add_task(task):
        task = task
        c.execute(f"INSERT INTO 'do_list' VALUES (?,?) ", ('❌', task))
    #loop for adding task multiple times
    adding = True
    while adding:
        task = input('What task would you like to add? (Leave empty to stop adding)')
        if task == '':
            adding = False
            continue
        add_task(task)
    conn.commit()

#Checking tasks
def checking():
    c.execute("SELECT * FROM do_list")
    my_data = c.fetchall()
    for i in my_data:
        print(i)

#Select your function
func = input('What would you like add a task(A), Check your tasks(C), Remove a task(R): ')
if func.upper() == 'A':
    adding()
elif func.upper() == 'C':
    checking()
conn.close()