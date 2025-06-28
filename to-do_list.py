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

#Finishing tasks
def finish():
    def finish_task(task):
        c.execute("UPDATE 'do_list' SET finished=? WHERE finished=? AND task=?", ('✅','❌', task))
    finished = True
    while finished:
        task = input('What tasks have you finished? (Leave empty to stop changing status): ')
        if task == '':
            finished = False
            continue
        finish_task(task)
        print ('✅ ' + task)
    conn.commit()
#Select your function
func = input('What would you like to do. Add a task(A), Check your tasks(C), Finish a task(F), Remove a task(R): ')
if func.upper() == 'A':
    adding()
elif func.upper() == 'C':
    checking()
elif func.upper() == 'F':
    finish()
conn.close()