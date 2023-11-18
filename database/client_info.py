import sqlite3 as sq 
from create_bot import bot
from aiogram.types import BotCommand,BotCommandScopeChat, CallbackQuery
import re
from aiogram.fsm.context import FSMContext



def sql_start():
    global db,cur 
    db=sq.connect("User_information.db")
    cur=db.cursor()

    if db:
        print('Data base connected OK!')
    cur.execute(""" CREATE TABLE IF NOT EXISTS info_users(full_name,phone,programming_languages,user_id,role,extra_role,payments,invite_people,cashback)""")
    db.commit()
    cur.execute("INSERT INTO info_users(full_name,phone,programming_languages,user_id,role,extra_role,payments,invite_people,cashback) VALUES(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL)")
    db.commit()



async def add_user_info(callback,state):
    data= await state.get_data()
    info=(data['name'],data['phone'],data['prg_languages'],data['user_id'])       
    cur.execute("""INSERT INTO info_users(full_name,phone,programming_languages,user_id) VALUES(?,?,?,?)""",info)
    db.commit()

async def show_user_id(message):
    cur.execute("SELECT user_id FROM info_users")
    check_id=cur.fetchall()
    for i in check_id:
        print(i)
    if int(message.from_user.id) in i:
        await message.answer('You have already registered from our bot ')
        await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations'),BotCommand(command='status',description='your monthly payments and cashback'),BotCommand(command='lesson', description='List of lessons'),BotCommand(command='courses',description='List of courses'),BotCommand(command='settings',description='Bot settings')],BotCommandScopeChat(chat_id=message.from_user.id))
    else:
        await bot.set_my_commands([BotCommand(command='register',description='Register to use our bot')],BotCommandScopeChat(chat_id=message.from_user.id))
        await message.answer('Register to use our bot')


async def role_user(callback,state):
    no_symbol=[]
    data= await state.get_data()
    role_info=[data['role'],data['name_role']]
    
    cur.execute('SELECT full_name FROM info_users')
    role_u=cur.fetchall()
    for i in role_u:
        no_symbol.append(re.sub("[(),'']",'',str(i)))
    print(no_symbol)
    if data['name_role'] in no_symbol:
        cur.execute('UPDATE info_users SET role=? WHERE full_name=?',role_info,)
        db.commit()
        await callback.message.answer('Your information has been saved')    
    else:
        await callback.message.answer('No such user')
        





