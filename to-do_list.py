#a to-do list
#features include: Adding a to-do, Checking the list, Finishing a to-do, Deleting a to-do, Making a new list
import sqlite3

conn = sqlite3.connect('/Users/Emad/Desktop/Github port/to-do/to-do-list.db')
c = conn.cursor()

c.execute(""" CREATE TABLE do_list (
            finished TEXT,
            task TEXT
        )
    """)

conn.commit()
conn.close()