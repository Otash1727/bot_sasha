import sqlite3 as sq 


def sql_start():
    global db,cur 
    db=sq.connect("Students_information.db")
    cur=db.cursor()

    if db:
        print('Data base connected OK!')
    cur.execute(""" CREATE TABLE IF NOT EXISTS info(user_id,full_name,phone)""")
    db.commit()

    


async def user_id_add(message):
    user_id1=("SELECT * FROM list_users WHERE users_id=?")
    user_id=(message.from_user.id,)
    cur.execute(user_id1,user_id)
    show_user_id=cur.fetchall()
    print(show_user_id)
    if show_user_id!=[]:
        for copy_id in show_user_id:
            copy_id
        if message.from_user.id in copy_id:
            await message.answer('You registered before \n Press the button ‘My account’ to start the test',reply_markup=account_markup)    
    else:
        await  message.answer('Send your phone number to use the bot',)