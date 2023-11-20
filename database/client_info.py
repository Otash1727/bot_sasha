import sqlite3 as sq 
from create_bot import bot
from aiogram.types import BotCommand,BotCommandScopeChat, CallbackQuery
import re
from aiogram.fsm.context import FSMContext
from keyboard import *


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

"""General function"""
async def show_userinfo():
    cur.execute("SELECT full_name FROM info_users")
    sh_i=cur.fetchall()
    return sh_i


""" PART MARKING THE ROLE PAYMETS,CASHBACK,PARTNERS """

"""Marking user role"""
async def role_user(callback,state):
    no_symbol=[]
    data= await state.get_data()
    role_info=[data['role'],data['name_role']]
    role_info2=[data['name_role'],]
    cur.execute('SELECT full_name FROM info_users')
    role_u=cur.fetchall()
    for i in role_u:
        no_symbol.append(re.sub("[(),'']",'',str(i)))
    if data['name_role'] in no_symbol:
        cur.execute('UPDATE info_users SET role=? WHERE full_name=?',role_info,)
        db.commit()
        cur.execute('SELECT full_name,role FROM info_users WHERE full_name=?',role_info2,)
        show_r=cur.fetchall()
        for ii in show_r:
            (re.sub("[(),'']",'',str(ii)))
        await callback.answer(f'Your information has been saved\n user-{ii[0]}\nrole-{ii[1]}',show_alert=True)    
    else:
        await callback.message.answer('No such user',reply_markup=admin_kb.add_info_kb)


""" List of payments"""

async def pay_user(callback,state):
    pay_symbol=[]
    data= await state.get_data()
    pay_info=[data['pay'],data['name_pay']]
    pay_info2=[data['name_pay'],]
    cur.execute('SELECT full_name FROM info_users')
    pay_u=cur.fetchall()
    for i in pay_u:
        pay_symbol.append(re.sub("[(),'']",'',str(i)))
    if data['name_pay'] in pay_symbol:
        cur.execute('UPDATE info_users SET payments=? WHERE full_name=?',pay_info,)
        db.commit()
        cur.execute('SELECT full_name,payments FROM info_users WHERE full_name=?',pay_info2,)
        show_p=cur.fetchall()
        for ii in show_p:
            (re.sub("[(),'']",'',str(ii)))
        await callback.answer(f'Your information has been saved\n user-{ii[0]}\npayments-{ii[1]}',show_alert=True)    
    else:
        await callback.message.answer('No such user',reply_markup=admin_kb.add_info_kb)
    
"""   List of partners"""
async def part_user(callback,state):    
    part_symbol=[]
    data= await state.get_data()
    part_info=[data['part'],data['name_part']]
    part_info2=[data['name_part'],]
    cur.execute('SELECT full_name FROM info_users')
    part_u=cur.fetchall()
    for i in part_u:
        part_symbol.append(re.sub("[(),'']",'',str(i)))
    if data['name_part'] in part_symbol:
        cur.execute('UPDATE info_users SET extra_role=? WHERE full_name=?',part_info,)
        db.commit()
        cur.execute('SELECT full_name,extra_role FROM info_users WHERE full_name=?',part_info2,)
        show_part=cur.fetchall()
        for ii in show_part:
            (re.sub("[(),'']",'',str(ii)))
        await callback.answer(f'Your information has been saved\n user-{ii[0]}\npartner-{ii[1]}',show_alert=True)    
    else:
        await callback.message.answer('No such user',reply_markup=admin_kb.add_info_kb)

""""Cashback"""
async def cash_user(callback,state): 
    cash_symbol=[]
    data= await state.get_data()
    cash_info=[data['cash'],data['name_cash']]
    cash_info2=[data['name_cash'],]
    cur.execute('SELECT full_name FROM info_users')
    cash_u=cur.fetchall()
    for i in cash_u:
        cash_symbol.append(re.sub("[(),'']",'',str(i)))
    if data['name_cash'] in cash_symbol:
        cur.execute('UPDATE info_users SET cashback=? WHERE full_name=?',cash_info,)
        db.commit()
        cur.execute('SELECT full_name,cashback FROM info_users WHERE full_name=?',cash_info2,)
        show_cash=cur.fetchall()
        for ii in show_cash:
            (re.sub("[(),'']",'',str(ii)))
        await callback.answer(f'Your information has been saved\n user-{ii[0]}\ncashback-{ii[1]}',show_alert=True)    
    else:
        await callback.message.answer('No such user',reply_markup=admin_kb.add_info_kb)       


""""PART-2  SEARCH IN ALL INFORMATION"""

async def find_all_catigories(message,state):
    cash_symbol=[]
    data= await state.get_data()
    catigories=[data['name_catigories'],]
    
    """Search by name"""
    cur.execute('SELECT * FROM info_users WHERE full_name=?',catigories)
    name_search=cur.fetchall()
    for имя in name_search:
        re.sub("[(),'']",'',str(имя))

    """Search by phone number"""
    cur.execute('SELECT * FROM info_users WHERE phone=?',catigories)
    phone_search=cur.fetchall()
    for тел in phone_search:
        re.sub("[(),'']",'',str(тел))

    """Search by programming languages"""
    cur.execute('SELECT * FROM info_users WHERE programming_languages=?',catigories)
    languages_search=cur.fetchall()
    for languages in languages_search:
        re.sub("[(),'']",'',str(languages))

    """Search by user_id"""
    cur.execute('SELECT * FROM info_users WHERE user_id=?',catigories)
    id_search=cur.fetchall()
    for idd in id_search:
        re.sub("[(),'']",'',str(idd))

    """Search by role"""
    cur.execute('SELECT * FROM info_users WHERE role=?',catigories)
    role_search=cur.fetchall()
    for role in role_search:
        re.sub("[(),'']",'',str(role))

    """Search by extra role"""
    cur.execute('SELECT * FROM info_users WHERE extra_role=?',catigories)
    extra_search=cur.fetchall()
    for extra in extra_search:
        re.sub("[(),'']",'',str(extra))

    """Search by payments"""
    cur.execute('SELECT * FROM info_users WHERE payments=?',catigories)
    pay_search=cur.fetchall()
    for payment in pay_search:
        re.sub("[(),'']",'',str(payment))

    """Search by invite_people"""
    cur.execute('SELECT * FROM info_users WHERE invite_people=?',catigories)
    people_search=cur.fetchall()
    for invite in people_search:
        re.sub("[(),'']",'',str(invite))

    """Search by cashback"""    
    cur.execute('SELECT * FROM info_users WHERE cashback=?',catigories)
    cash_search=cur.fetchall()
    for cashback in cash_search:
        re.sub("[(),'']",'',str(cashback))
    
    try:
        if имя!=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for имя in name_search:
            re.sub("[(),'']",'',str(имя))
            await message.answer(f"Student - {имя[0]}\nPhone number - {имя[1]}\nProgramming languages - {имя[2]}\nUser_id - {имя[3]}\nRole - {имя[4]}\nExtra role - {имя[5]}\nMonthly payment - {имя[6]},\nInvited poeple- {имя[7]}\nCashback - {имя[8]} ")
    
    try:
        if тел!=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for имя in name_search:
            re.sub("[(),'']",'',str(тел))
            await message.answer(f"Student - {тел[0]}\nPhone number - {тел[1]}\nProgramming languages - {тел[2]}\nUser_id - {тел[3]}\nRole - {тел[4]}\nExtra role - {тел[5]}\nMonthly payment - {тел[6]},\nInvited poeple- {тел[7]}\nCashback - {тел[8]} ")

    try:
        if languages!=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for languages in languages_search:
            re.sub("[(),'']",'',str(languages))
            await message.answer(f"Student - {languages[0]}\nPhone number - {languages[1]}\nProgramming languages - {languages[2]}\nUser_id - {languages[3]}\nRole - {languages[4]}\nExtra role - {languages[5]}\nMonthly payment - {languages[6]},\nInvited poeple- {languages[7]}\nCashback - {languages[8]} ")

    try:
        if idd!=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for idd  in name_search:
            re.sub("[(),'']",'',str(idd))
        await message.answer(f"Student - {idd[0]}\nPhone number - {idd[1]}\nProgramming languages - {idd[2]}\nUser_id - {idd[3]}\nRole - {idd[4]}\nExtra role - {idd[5]}\nMonthly payment - {idd[6]},\nInvited poeple- {idd[7]}\nCashback - {idd[8]} ")
    
    try:
        if role!=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for role in name_search:
            re.sub("[(),'']",'',str(role))
        await message.answer(f"Student - {role[0]}\nPhone number - {role[1]}\nProgramming languages - {role[2]}\nUser_id - {role[3]}\nRole - {role[4]}\nExtra role - {role[5]}\nMonthly payment - {role[6]},\nInvited poeple- {role[7]}\nCashback - {role[8]} ")

    try:
        if extra !=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for extra in name_search:
            re.sub("[(),'']",'',str(extra))
        await message.answer(f"Student - {extra[0]}\nPhone number - {extra[1]}\nProgramming languages - {extra[2]}\nUser_id - {extra[3]}\nRole - {extra[4]}\nExtra role - {extra[5]}\nMonthly payment - {extra[6]},\nInvited poeple- {extra[7]}\nCashback - {extra[8]} ")

    try:
        if payment !=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for payment in name_search:
            re.sub("[(),'']",'',str(payment))
        await message.answer(f"Student - {payment[0]}\nPhone number - {payment[1]}\nProgramming languages - {payment[2]}\nUser_id - {payment[3]}\nRole - {payment[4]}\nExtra role - {payment[5]}\nMonthly payment - {payment[6]},\nInvited poeple- {payment[7]}\nCashback - {payment[8]} ")

    try:
        if invite !=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for invite in name_search:
            re.sub("[(),'']",'',str(invite))
        await message.answer(f"Student - {invite[0]}\nPhone number - {invite[1]}\nProgramming languages - {invite[2]}\nUser_id - {invite[3]}\nRole - {invite[4]}\nExtra role - {invite[5]}\nMonthly payment - {invite[6]},\nInvited poeple- {invite[7]}\nCashback - {invite[8]} ")

    try:
        if cashback!=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for cashback in name_search:
            re.sub("[(),'']",'',str(cashback))
        await message.answer(f"Student - {cashback[0]}\nPhone number - {cashback[1]}\nProgramming languages - {cashback[2]}\nUser_id - {cashback[3]}\nRole - {cashback[4]}\nExtra role - {cashback[5]}\nMonthly payment - {cashback[6]},\nInvited poeple- {cashback[7]}\nCashback - {cashback[8]} ")
    try:
        if extra!=[] and cashback!=[] and  idd!=[] and role!=[] and payment!=[] and invite!=[] and languages!=[] and имя!=[]  



#idd,role,extra,payment,invite,cashback