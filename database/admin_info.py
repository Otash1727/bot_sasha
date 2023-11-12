import sqlite3 as sq 
import re   


def sql_start_admin():
    global db_admin,cur_admin
    db_admin=sq.connect('Admin_info.db',timeout=15)
    cur_admin=db_admin.cursor()

    if db_admin:
        print('Admin_Database is connectting...')
    cur_admin.execute(""" CREATE TABLE IF NOT EXISTS admin_info(password)""")
    db_admin.commit()

async def old_pass(path):
    cur_admin.execute("INSERT INTO admin_info VALUES(?)",path,)
    db_admin.commit()

async def update_pass(message,state):
    data= await state.get_data()
    path=(data['new_path'])
    print(path)
    cur_admin.execute("SELECT password FROM admin_info")
    show_pass=cur_admin.fetchall()
    for i in show_pass:
        i
    old_path=(re.sub("[(),'']",'', str(i)))
    print(old_path)
    
    cur_admin.execute("UPDATE admin_info SET password=? WHERE password=?",(path,old_path,))
    db_admin.commit()

async def show_path(message,update_builder):
    cur_admin.execute("SELECT password FROM admin_info")
    show_pass=cur_admin.fetchall()
    for i in (show_pass):
        i
    await message.answer(f" Your old password \n {re.sub('[(),'']','', str(i))}",reply_markup=update_builder.as_markup())


async def get_pass():
    cur_admin.execute("SELECT password FROM admin_info")
    get_path=cur_admin.fetchall()
    for i in (get_path):
        i
    return  re.sub("[(),'']",'', str(i))
        
   
