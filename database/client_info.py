import sqlite3 as sq 
from create_bot import bot
from aiogram.types import BotCommand,BotCommandScopeChat, CallbackQuery
import re
from aiogram.fsm.context import FSMContext
from keyboard import admin_kb


def sql_start():
    global db,cur 
    db=sq.connect("User_information.db")
    cur=db.cursor()

    if db:
        print('Data base connected OK!')
    cur.execute(""" CREATE TABLE IF NOT EXISTS info_users(name,sur_name,phone,programming_languages,user_id,role,extra_role,payments,invite_people,cashback)""")
    db.commit()
    cur.execute("INSERT INTO info_users(name,sur_name,phone,programming_languages,user_id,role,extra_role,payments,invite_people,cashback) VALUES(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL)")
    db.commit()


""" Client info"""
async def add_user_info(callback,state):
    data= await state.get_data()
    info=(data['name'],data['sur_name'],data['phone'],data['prg_languages'],data['user_id'])       
    cur.execute("""INSERT INTO info_users(name,sur_name,phone,programming_languages,user_id) VALUES(?,?,?,?,?)""",info)
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
    cur.execute("SELECT name FROM info_users")
    sh_i=cur.fetchall()
    return sh_i

async def show_surname():
    cur.execute('SELECT sur_name FROM info_users')
    sh_s=cur.fetchall()
    return sh_s

""" PART MARKING THE ROLE PAYMETS,CASHBACK,PARTNERS """

"""Marking user role"""
async def role_user(callback,state):
    no_symbol=[]
    no_symbol2=[]
    data= await state.get_data()
    role_info=[data['role'],data['name_role']]
    role_info2=[data['name_role'],]
    cur.execute('SELECT name FROM info_users')
    role_u=cur.fetchall()
    cur.execute('SELECT sur_name FROM info_users')
    role_s=cur.fetchall()
    # Search by name
    for i in role_u:
        no_symbol.append(re.sub("[(),'']",'',str(i)))
    if data['name_role'] in no_symbol:
        cur.execute('UPDATE info_users SET role=? WHERE name=?,sur_name=?',role_info,)
        db.commit()
        cur.execute('SELECT name,sur_name,role FROM info_users WHERE name=?',role_info2,)
        show_r=cur.fetchall()
        for ii in show_r:
            (re.sub("[(),'']",'',str(ii)))
        await callback.answer(f'Your information has been saved\n users name-{ii[0]}\nusers surname {i[1]}\nrole-{ii[2]}',show_alert=True)    
    # Search by surname
    for ii in role_s:
        no_symbol2.append(re.sub("[(),'']",'',str(ii)))
    if data['name_role'] in no_symbol2:
        cur.execute('UPDATE info_users SET role=? WHERE sur_name=?',role_info,)
        db.commit()
        cur.execute('SELECT name,sur_name,role FROM info_users WHERE sur_name=?',role_info2,)
        show_s=cur.fetchall()
        for ii3 in show_s:
            (re.sub("[(),'']",'',str(ii3)))
        await callback.answer(f'Your information has been saved\n users name-{ii3[0]}\nusers surname {ii3[1]}\nrole-{ii3[2]}',show_alert=True) 
   


""" List of payments"""

async def pay_user(callback,state):
    pay_symbol=[]
    pay_symbol2=[]
    data= await state.get_data()
    pay_info=[data['pay'],data['name_pay']]
    pay_info2=[data['name_pay'],]
    # copy by name in database
    cur.execute('SELECT name FROM info_users')
    pay_u=cur.fetchall()
    #copy by surname in database
    cur.execute('SELECT sur_name FROM info_users')
    pay_s=cur.fetchall()
    
    for i in pay_u:
        pay_symbol.append(re.sub("[(),'']",'',str(i)))
    
    for ii in pay_s:
        pay_symbol2.append(re.sub("[(),'']",'',str(ii)))
    #Check by name 
    if data['name_pay'] in pay_symbol:
        cur.execute('UPDATE info_users SET payments=? WHERE name=?',pay_info,)
        db.commit()
        cur.execute('SELECT name,sur_name,payments FROM info_users WHERE name=?',pay_info2,)
        show_p=cur.fetchall()
        for iii in show_p:
            (re.sub("[(),'']",'',str(iii.capitalaze())))
        await callback.answer(f'Your information has been saved\n user-{ii[0]},\n surname - {i[1]}\npayments-{ii[2]}',show_alert=True)    
    #check ny surname
    if data['name_pay'] in pay_symbol2:
        cur.execute('UPDATE info_users SET payments=? WHERE sur_name=?',pay_info,)
        db.commit()
        cur.execute('SELECT name,sur_name,payments FROM info_users WHERE sur_name=?',pay_info2,)
        show_p=cur.fetchall()
        for i4 in show_p:
            (re.sub("[(),'']",'',str(i4)))
        await callback.answer(f'Your information has been saved\n user-{i4[0]},\nsurname - {i4[1]},\npayments-{i4[2]}',show_alert=True)
    
    
"""   List of partners"""
async def part_user(callback,state):    
    part_symbol=[]
    part_symbol2=[]
    data= await state.get_data()
    part_info=[data['part'],data['name_part']]
    part_info2=[data['name_part'],]
    #copy by name in database
    cur.execute('SELECT name FROM info_users')
    part_u=cur.fetchall()
    #copy by surname in database
    cur.execute('SELECT sur_name FROM info_users')
    part_s=cur.fetchall()
    
    for i in part_u:
        part_symbol.append(re.sub("[(),'']",'',str(i)))

    for ii in part_s:
        part_symbol2.append(re.sub("[(),'']",'',str(ii)))
    #check by name 
    if data['name_part'] in part_symbol:
        cur.execute('UPDATE info_users SET extra_role=? WHERE name=?',part_info,)
        db.commit()
        cur.execute('SELECT name,sur_name,extra_role FROM info_users WHERE name=?',part_info2,)
        show_part=cur.fetchall()
        for ii in show_part:
            (re.sub("[(),'']",'',str(ii)))
        await callback.answer(f'Your information has been saved\nuser name - {ii[0]}\nuser surname - {ii[1]}\npartner - {ii[2]}',show_alert=True)    
    # check by surname
    if data['name_part'] in part_symbol2:
        cur.execute('UPDATE info_users SET extra_role=? WHERE sur_name=?',part_info,)
        db.commit()
        cur.execute('SELECT name,sur_name,extra_role FROM info_users WHERE sur_name=?',part_info2,)
        show_part=cur.fetchall()
        for ii in show_part:
            (re.sub("[(),'']",'',str(ii)))
        await callback.answer(f'Your information has been saved\nuser name -{ii[0]}\nuser surname - {ii[1]}\npartner-{ii[2]}',show_alert=True)    
    

""""Cashback"""
async def cash_user(callback,state): 
    cash_symbol=[]
    cash_symbol2=[]
    data= await state.get_data()
    cash_info=[data['cash'],data['name_cash']]
    cash_info2=[data['name_cash'],]
    # copy by name in database
    cur.execute('SELECT name FROM info_users')
    cash_u=cur.fetchall()
    #copy by surname in database
    cur.execute('SELECT sur_name FROM info_users')
    cash_s=cur.fetchall()
    
    for i in cash_u:
        cash_symbol.append(re.sub("[(),'']",'',str(i)))
    
    for ii in cash_s:
        cash_symbol2.append(re.sub("[(),'']",'',str(ii)))
    # check by name 
    if data['name_cash'] in cash_symbol:
        cur.execute('UPDATE info_users SET cashback=? WHERE name=?',cash_info,)
        db.commit()
        cur.execute('SELECT name,sur_name,cashback FROM info_users WHERE name=?',cash_info2,)
        show_cash=cur.fetchall()
        for ii in show_cash:
            (re.sub("[(),'']",'',str(ii)))
        await callback.answer(f'Your information has been saved\nuser - {ii[0]}\nuser surname - {ii[1]}\ncashback - {ii[2]}',show_alert=True)    
    # check by surname
    if data['name_cash'] in cash_symbol2:
        cur.execute('UPDATE info_users SET cashback=? WHERE sur_name=?',cash_info,)
        db.commit()
        cur.execute('SELECT name,sur_name,cashback FROM info_users WHERE sur_name=?',cash_info2,)
        show_sur=cur.fetchall()
        for ii in show_sur:
            (re.sub("[(),'']",'',str(ii)))
        await callback.answer(f'Your information has been saved\nuser - {ii[0]}\nuser surname - {ii[1]}\ncashback - {ii[2]}',show_alert=True)    
           

""""PART-2  SEARCH IN ALL INFORMATION"""

async def find_all_catigories(message,state):
    cash_symbol=[]
    data= await state.get_data()
    catigories=[(data['name_catigories']),]
    
    """Search by name"""
    cur.execute('SELECT * FROM info_users WHERE name=?',catigories)
    name_search=cur.fetchall()
    for имя in name_search:
        re.sub("[(),'']",'',str(имя))

    """Search by surname"""
    cur.execute('SELECT * FROM info_users WHERE sur_name=?',catigories)
    surname_search=cur.fetchall()
    for full_name in surname_search:
        re.sub("[(),'']",'',str(full_name))

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
    
    """Search by transaction"""
    
    try:
        if имя!=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for имя in name_search:
            re.sub("[(),'']",'',str(имя))
            await message.answer(f"Student - {имя[0]} {имя[1]}\nPhone number - {имя[2]}\nProgramming languages - {имя[3]}\nUser_id - {имя[4]}\nRole - {имя[5]}\nExtra role - {имя[6]}\nMonthly payment - {имя[7]},\nInvited poeple- {имя[8]}\nCashback - {имя[9]} ")
    
    try:
        if full_name!=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for full_name in surname_search:
            re.sub("[(),'']",'',str(full_name))
            await message.answer(f"Student's - {full_name[0]} {full_name[1]}\nPhone number - {full_name[2]}\nProgramming languages - {full_name[3]}\nUser_id - {full_name[4]}\nRole - {full_name[5]}\nExtra role - {full_name[6]}\nMonthly payment - {full_name[7]},\nInvited poeple- {full_name[8]}\nCashback - {full_name[9]} ")
    
    try:
        if тел!=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for тел in phone_search:
            re.sub("[(),'']",'',str(тел))
            await message.answer(f"Student - {тел[0]} {тел[1]}\nPhone number - {тел[2]}\nProgramming languages - {тел[3]}\nUser_id - {тел[4]}\nRole - {тел[5]}\nExtra role - {тел[6]}\nMonthly payment - {тел[7]},\nInvited poeple- {тел[8]}\nCashback - {тел[9]} ")

    try:
        if languages!=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for languages in languages_search:
            re.sub("[(),'']",'',str(languages))
            await message.answer(f"Student - {languages[0]} {languages[1]}\nPhone number - {languages[2]}\nProgramming languages - {languages[3]}\nUser_id - {languages[4]}\nRole - {languages[5]}\nExtra role - {languages[6]}\nMonthly payment - {languages[7]},\nInvited poeple- {languages[8]}\nCashback - {languages[9]} ")

    try:
        if idd!=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for idd  in id_search:
            re.sub("[(),'']",'',str(idd))
        await message.answer(f"Student - {idd[0]} {idd[1]}\nPhone number - {idd[2]}\nProgramming languages - {idd[3]}\nUser_id - {idd[4]}\nRole - {idd[5]}\nExtra role - {idd[6]}\nMonthly payment - {idd[7]},\nInvited poeple- {idd[8]}\nCashback - {idd[9]} ")
    
    try:
        if role!=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for role in role_search:
            re.sub("[(),'']",'',str(role))
        await message.answer(f"Student - {role[0]} {role[1]}\nPhone number - {role[2]}\nProgramming languages - {role[3]}\nUser_id - {role[4]}\nRole - {role[5]}\nExtra role - {role[6]}\nMonthly payment - {role[7]},\nInvited poeple- {role[8]}\nCashback - {role[9]} ")

    try:
        if extra !=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for extra in extra_search:
            re.sub("[(),'']",'',str(extra))
        await message.answer(f"Student - {extra[0]}  {extra[1]}\nPhone number - {extra[2]}\nProgramming languages - {extra[3]}\nUser_id - {extra[4]}\nRole - {extra[5]}\nExtra role - {extra[6]}\nMonthly payment - {extra[7]},\nInvited poeple- {extra[8]}\nCashback - {extra[9]} ")

    try:
        if payment !=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for payment in pay_search:
            re.sub("[(),'']",'',str(payment))
        await message.answer(f"Student - {payment[0]} {payment[1]}\nPhone number - {payment[2]}\nProgramming languages - {payment[3]}\nUser_id - {payment[4]}\nRole - {payment[5]}\nExtra role - {payment[6]}\nMonthly payment - {payment[7]},\nInvited poeple- {payment[8]}\nCashback - {payment[9]} ")

    try:
        if invite !=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for invite in people_search:
            re.sub("[(),'']",'',str(invite))
        await message.answer(f"Student - {invite[0]} {invite[1]}\nPhone number - {invite[2]}\nProgramming languages - {invite[3]}\nUser_id - {invite[4]}\nRole - {invite[5]}\nExtra role - {invite[6]}\nMonthly payment - {invite[7]},\nInvited poeple- {invite[8]}\nCashback - {invite[9]} ")

    try:
        if cashback!=[]:
            print(1)
    except UnboundLocalError:
        print(0)
    else:
        for cashback in cash_search:
            re.sub("[(),'']",'',str(cashback))
        await message.answer(f"Student - {cashback[0]}  {cashback[1]}\nPhone number - {cashback[2]}\nProgramming languages - {cashback[3]}\nUser_id - {cashback[4]}\nRole - {cashback[5]}\nExtra role - {cashback[6]}\nMonthly payment - {cashback[7]},\nInvited poeple- {cashback[8]}\nCashback - {cashback[9]} ")
   #try:
   #    if extra!=[] and cashback!=[] and  idd!=[] and role!=[] and payment!=[] and invite!=[] and languages!=[] and имя!=[] and тел!=[]:
   #        print('Information not found')
   #except UnboundLocalError:
""" PART 3 Group  """

async def show_list(callback,state):
    data= await state.get_data()
    info_group=[data['name_group']]
    cur.execute("SELECT name,sur_name,programming_languages FROM info_users WHERE programming_languages=?",info_group,)
    show_group_list=cur.fetchall()
    for i in show_group_list:
        re.sub("[(),'']",'' , str(i))
    try:
        if i!=[]:
            print(1)
    except UnboundLocalError:
        await callback.message.answer('Not found information')
    else:
        for i in show_group_list:
            re.sub("[(),'']",'' , str(i))    
        await callback.message.answer(f"Student's- {i[0]} {i[1]}\nProgramming languages - {i[2]}")

"""PArt 4 transaction"""   

async def transaction_info(state,message):
    data= await state.get_data()
    trans=[data['name_transaction']]
    """ Search by full_name """
    cur.execute("SELECT payments,cashback FROM info_users WHERE full_name=?",trans,)
    trans_name=cur.fetchall()
    cur.execute("SELECT payments,cashback FROM info_users WHERE full_name=?",trans,)
    trans_name=cur.fetchall()


