import sqlite3 as sq 


def sql_start():
    global db,cur 
    db=sq.connect("Students_information.db")
    cur=db.cursor()

    if db:
        print('Data base connected OK!')
    cur.execute(""" CREATE TABLE IF NOT EXISTS info_users(full_name,phone,programming_languages,user_id)""")
    db.commit()



async def add_user_info(message,state):
    data= await state.get_data()
    info=(data['name'],data['phone'],data['prg_languages'],data['user_id'])       
    cur.execute("""INSERT INTO info_users(full_name,phone,programming_languages,user_id) VALUES(?,?,?,?)""",info)
    db.commit()

    

