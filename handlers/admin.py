from aiogram import F,Router
from aiogram.types import Message,CallbackQuery,KeyboardButton,ReplyKeyboardMarkup,Message,BotCommand,BotCommandScopeChat,CallbackQuery,BotCommandScopeDefault
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder,InlineKeyboardButton,KeyboardBuilder 
from aiogram.methods.delete_my_commands import DeleteMyCommands  
from aiogram.filters import Command, CommandStart, Filter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from aiogram.utils.formatting import Text
from keyboard import admin_kb
from database import *
from create_bot import bot
import re


router_admin=Router()



#class Update_path(StatesGroup):
#    role=State()
#    extra_role=State()
#    payments=State()
#    invite_people=State()
#    cashback=State()

class Role_path(StatesGroup):
    name_role=State()
    role=State()

class Payments_path(StatesGroup):
    name_pay=State()
    pay=State()

class Partners_path(StatesGroup):
    name_part=State()
    part=State()

class Cashback_path(StatesGroup):
    name_cash=State()
    cash=State()

class Search_catigories(StatesGroup):
    name_catigories=State()

class Group(StatesGroup):
    name_group=State()

class Transaction(StatesGroup):
    name_transaction=State()


"""  admin commands:
        /find
        /create
        /transactions
        /list of groups, courses, teachers, students, 
        /group
        /settings"""


@router_admin.message(Command('cyberhub'))
async def admin_window_open(message:Message):   
    await message.answer(f'Welcome {message.from_user.full_name}')
    await bot.set_my_commands([BotCommand(command='menu',description='Show catalog menu'),BotCommand(command='add',description='add the bot to catalog'),BotCommand(command='setlanguaeges',description='Set bot languages')],BotCommandScopeChat(chat_id=message.from_user.id))
    """ admin deb belgilangan royhatdan olish kerak user_id ni"""


@router_admin.message(Command('menu'))
async def find_info(message:Message):
    await message.answer('You are in admin panel of cyberhub bot', reply_markup=admin_kb.admin_window_kb)



@router_admin.callback_query(F.data=='schoolinfo')
async def add_base(callback:CallbackQuery):
    await callback.message.answer('This is where you add information. Select categories',reply_markup=admin_kb.add_info_kb)


""" PART MARKING THE ROLE PAYMENTS, PARTNERS CASHBACK"""

"""Marking user role"""

@router_admin.callback_query(F.data=='Mrole')
async def mark_role(callback:CallbackQuery,state:FSMContext):
    await state.set_state(Role_path.name_role)
    await callback.answer('Input student\'s name',show_alert=True)

@router_admin.message(Role_path.name_role)
async def mark_name(message:Message,state:FSMContext):
    ff=[]
    fff=[]
    data=await state.update_data(name_role=message.text.lower())
    dd=await client_info.show_userinfo()
    ddd=await client_info.show_surname()
    for i in dd:
        ff.append(re.sub("[(),'']",'',str(i)))
    for ii in ddd:
        fff.append(re.sub("[(),'']",'',str(ii)))
    if data['name_role'] in ff:
        await message.answer(f"{data['name_role']}\n Select role")
        await state.set_state(Role_path.role)
    if data['name_role'] in fff:
        await message.answer(f"{data['name_role']}\n Select role")
        await state.set_state(Role_path.role)
    else:
        await message.answer('No such user',reply_markup=admin_kb.add_info_kb)
        await state.clear()        
            
@router_admin.message(Role_path.role)
async def mark_role(message:Message,state:FSMContext):
    data= await state.update_data(role=message.text)
    role_search=InlineKeyboardBuilder()
    role_search.add(InlineKeyboardButton(text=f"{data['role']}\n save",callback_data='main_role'))
    await message.answer('Are you sure?', reply_markup=role_search.as_markup())    

@router_admin.callback_query(F.data=='main_role')
async def save_role(callback:CallbackQuery, state:FSMContext): 
    await client_info.role_user(callback,state)
    await state.clear()

"""List of payments"""

@router_admin.callback_query(F.data=='Lpayments')
async def mark_pay(callback:CallbackQuery,state:FSMContext):
    await state.set_state(Payments_path.name_pay)
    await callback.answer('Please. Input student\'s name',show_alert=True)

@router_admin.message(Payments_path.name_pay)
async def payment_name(message:Message,state:FSMContext):
    pay_list=[]
    pay_surname=[]
    data=await state.update_data(name_pay=message.text.lower())
    dd=await client_info.show_userinfo() 
    ddd= await client_info.show_surname()
    #copy by name 
    for i in dd:
      pay_list.append(re.sub("[(),'']",'',str(i)))
    #Copy by surname
    for ii in ddd:
      pay_surname.append(re.sub("[(),'']",'',str(ii)))
    if data['name_pay'] in pay_list:
        await message.answer(f"{data['name_pay']}\n Enter payment info")
        await state.set_state(Payments_path.pay)
    elif data['name_pay'] in pay_surname:
        await message.answer(f"{data['name_pay']}\n Enter payment info")
        await state.set_state(Payments_path.pay)     
    else:
        await message.answer('No such user',reply_markup=admin_kb.add_info_kb)
        await state.clear()

@router_admin.message(Payments_path.pay)
async def enter_pay(message:Message,state:FSMContext):
    data=await state.update_data(pay=message.text.lower())
    pay_search=InlineKeyboardBuilder()
    pay_search.add(InlineKeyboardButton(text=f"{data['pay']}\n Save",callback_data='main_pay'))
    await message.answer('Are you sure?', reply_markup=pay_search.as_markup())

@router_admin.callback_query(F.data=='main_pay')
async def save_role(callback:CallbackQuery, state:FSMContext): 
    await client_info.pay_user(callback, state)
    await state.clear()

""" List of partners """
@router_admin.callback_query(F.data=='partners')
async def mark_part(callback:CallbackQuery,state:FSMContext):
    await state.set_state(Partners_path.name_part)
    await callback.answer("Please. Enter student\'s name",show_alert=True)

@router_admin.message(Partners_path.name_part)
async def partners_name(message:Message,state:FSMContext):
    part_list=[]
    part_surname=[]
    data=await state.update_data(name_part=message.text.lower())
    dd=await client_info.show_userinfo() 
    ddd=await client_info.show_surname()
    #copy by name 
    for i in dd:
      part_list.append(re.sub("[(),'']",'',str(i)))
    
    #copy by surname
    for ii in ddd:
      part_surname.append(re.sub("[(),'']",'',str(ii)))
    
    if data['name_part'] in part_list:
        await message.answer(f"{data['name_part']}\n Enter partners info")
        await state.set_state(Partners_path.part) 
    
    elif data['name_part'] in part_surname:
        await message.answer(f"{data['name_part']}\n Enter partners info")
        await state.set_state(Partners_path.part) 
    else:
        await message.answer('No such user',reply_markup=admin_kb.add_info_kb)
        await state.clear()
        

@router_admin.message(Partners_path.part)
async def enter_part(message:Message,state:FSMContext):
    data=await state.update_data(part=message.text.lower())
    part_search=InlineKeyboardBuilder()
    part_search.add(InlineKeyboardButton(text=f"{data['part']}\n Save",callback_data='main_part'))
    await message.answer('Are you sure?', reply_markup=part_search.as_markup())

@router_admin.callback_query(F.data=='main_part')
async def save_role(callback:CallbackQuery, state:FSMContext): 
    await client_info.part_user(callback,state)
    await state.clear()

""""Cashback"""
@router_admin.callback_query(F.data=='cashback')
async def mark_cash(callback:CallbackQuery,state:FSMContext):
    await state.set_state(Cashback_path.name_cash)
    await callback.answer("Please. Enter student\'s name",show_alert=True)

@router_admin.message(Cashback_path.name_cash)
async def cashback_name(message:Message,state:FSMContext):
    cash_list=[]
    cash_surname=[]
    data=await state.update_data(name_cash=message.text.lower())
    dd=await client_info.show_userinfo() 
    ddd= await client_info.show_surname()
    # copy by name
    for i in dd:
      cash_list.append(re.sub("[(),'']",'',str(i)))
    # copy by surname
    for ii in ddd:
      cash_surname.append(re.sub("[(),'']",'',str(ii)))  
    
    if data['name_cash'] in cash_list:
        await message.answer(f"{data['name_cash']}\n Enter the student's cashback details")
        await state.set_state(Cashback_path.cash) 
   
    elif data['name_cash'] in cash_surname:
        await message.answer(f"{data['name_cash']}\n Enter the student's cashback details")
        await state.set_state(Cashback_path.cash) 
    
    else:
        await message.answer('No such user',reply_markup=admin_kb.add_info_kb)
        await state.clear()

@router_admin.message(Cashback_path.cash)
async def enter_cash(message:Message,state:FSMContext):
    data=await state.update_data(cash=message.text.lower())
    cash_search=InlineKeyboardBuilder()
    cash_search.add(InlineKeyboardButton(text=f"{data['cash']}\n Save",callback_data='main_cash'))
    await message.answer('Are you sure?', reply_markup=cash_search.as_markup())

@router_admin.callback_query(F.data=='main_cash')
async def save_cash(callback:CallbackQuery, state:FSMContext): 
    await client_info.cash_user(callback,state)
    await state.clear()


"""" PART-2 SEARCH IN ALL INFORMATION """
@router_admin.callback_query(F.data=='find')
async def search_info(callback:CallbackQuery,state:FSMContext):
    await callback.answer('Type the information you want to search for\n Enter information',show_alert=True)
    await state.set_state(Search_catigories.name_catigories)
    
@router_admin.message(Search_catigories.name_catigories)
async def  search_fsm(message:Message,state:FSMContext):
    await state.update_data(name_catigories=message.text.lower())
    await client_info.find_all_catigories(message=message,state=state) 
    await state.clear()  

""" PART 3 group"""

@router_admin.callback_query(F.data=='group')
async def group_list(callback:CallbackQuery, state:FSMContext):
    await callback.message.answer('Which group would you like to know about ?',reply_markup=admin_kb.list_group)
    await state.set_state(Group.name_group)

@router_admin.callback_query(F.data=='python_group',Group.name_group)
@router_admin.callback_query(F.data=='php_group',Group.name_group)
@router_admin.callback_query(F.data=='htmlcss_group',Group.name_group)
async def show_group(callback:CallbackQuery,state:FSMContext):
    if callback.data=='python_group':
        await state.update_data(name_group='python')
        await client_info.show_list(callback,state)
    if callback.data=='php_group':
        await state.update_data(name_group='php')
        await client_info.show_list(callback,state)
    if callback.data=='htmlcss_group':
        await state.update_data(name_group='htmlcss')
        await client_info.show_list(callback,state)
    await state.clear()

"""PART 4 transaction"""

@router_admin.callback_query(F.data=='transaction')
async def transaction_history(callback:CallbackQuery):
    await callback.message.answer("Would you like to know about transaction informations\n Enter Student's  name or surname or monthly payment info or cashback info, group",reply_markup=admin_kb.transaction_kb)

@router_admin.callback_query(F.data=='by_group')
async def find_transaction(callback:CallbackQuery,state:FSMContext):
    await state.set_state(Transaction.name_transaction)
    await callback.message.answer("Choose the group",reply_markup=admin_kb.list_group)

@router_admin.callback_query(F.data=='python_group',Transaction.name_transaction)
@router_admin.callback_query(F.data=='php_group',Transaction.name_transaction)
@router_admin.callback_query(F.data=='htmlcss_group',Transaction.name_transaction)
async def show_group(callback:CallbackQuery,state:FSMContext):
    if callback.data=='python_group':
        await state.update_data(name_group='python')
        await client_info.show_transaction(callback,state)
    if callback.data=='php_group':
        await state.update_data(name_group='php')
        await client_info.show_transaction(callback,state)
    if callback.data=='htmlcss_group':
        await state.update_data(name_group='htmlcss')
        await client_info.show_transaction(callback,state)
    await state.clear()

@router_admin.callback_query(F.data=='other_catigories')
async def find_other(callback:CallbackQuery, state:FSMContext):
    await callback.answer('Enter the data type',show_alert=True)
    await state.set_state(Transaction.name_transaction)

@router_admin.message(Transaction.name_transaction)
async def get_find(message:Message, state:FSMContext):
    data=await state.update_data(name_transaction=message.text.lower())
    await client_info.other_catigories(message=message,state=state)
    await state.clear() 