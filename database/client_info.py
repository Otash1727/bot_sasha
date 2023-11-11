import sqlite3 as sq 


def sql_start():
    global db,cur 
    db=sq.connect("Students_information.db")
    cur=db.cursor()

    if db:
        print('Data base connected OK!')
    cur.execute(""" CREATE TABLE IF NOT EXISTS info(user_id,full_name,phone)""")
    db.commit()

    

