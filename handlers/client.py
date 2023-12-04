from aiogram import Router ,F
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder,InlineKeyboardButton,KeyboardBuilder 
from aiogram.utils.deep_linking import decode_payload,create_deep_link
from aiogram.types import Message,BotCommand,BotCommandScopeChat,CallbackQuery,BotCommandScopeDefault,InlineQuery,InlineQueryResultArticle
from aiogram.methods.delete_my_commands import DeleteMyCommands
from aiogram.utils.formatting import Text, Bold
from aiogram.filters import Command, CommandStart, Filter
from aiogram.enums.content_type import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboard import client_kb
from database import client_info
import logging
import time
from create_bot import bot 
import re


router=Router()


class Form(StatesGroup):
    name=State()
    phone=State()
    user_id=State()
    #prg_languages=State()
    

   
@router.message(Command('start'))
async def cdm_start(message:Message,state:FSMContext):
    tg_id=[]
    data= await client_info.show_user_id()
    for i in data:
        tg_id.append(re.sub("[(),'']",'',str(i)))
    if str(message.from_user.id) in str(tg_id):
        await message.answer('You have already registered from our bot \n Please select the commands to use the bot')
        await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations'),BotCommand(command='status',description='your monthly payments and cashback'),BotCommand(command='lesson', description='List of lessons'),BotCommand(command='courses',description='List of courses'),BotCommand(command='settings',description='Bot settings')],BotCommandScopeChat(chat_id=message.from_user.id))
    else:
        await message.answer('Hi!. Welcome to the IT park of the bot',reply_markup=client_kb.start_up)
        #await message.answer('Hello you want to register our bot. Please input your name')
        
@router.callback_query(F.data=='signup')
async def startup (callback:CallbackQuery,state:FSMContext):
    await state.set_state(Form.name)
    await callback.message.answer('Input your name')

@router.message(Form.name)
async def input_name(message:Message, state:FSMContext):
    await state.update_data(name=message.text.lower())
    await state.update_data(user_id=message.from_user.id)
    await message.answer(f"Okey now you need to send your phone number", reply_markup=client_kb.contact_markup)
    await state.set_state(Form.phone)

@router.message(Form.phone)
async def input_phone(message:Message,state:FSMContext):
    phoneNumber = message.contact.phone_number if message.contact is not None else message.text
    data=await state.update_data(phone=phoneNumber)
    print(data['user_id'],data['phone'])
    if data['phone']!=None:
        await bot.send_message(chat_id=message.from_user.id,text='Thanks',reply_markup=client_kb.contact_remove)
        await client_info.add_user_info(state)
        await state.clear() 
        await message.answer('You have registed \n Please select the commands to use the bot')
        await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations'),BotCommand(command='status',description='your monthly payments and cashback'),BotCommand(command='lesson', description='List of lessons'),BotCommand(command='courses',description='List of courses'),BotCommand(command='settings',description='Bot settings')],BotCommandScopeChat(chat_id=message.from_user.id)) 

@router.callback_query(F.data=='skip')
async def skip_command(callback:CallbackQuery):
    await callback.message.answer('You can find out about us here',reply_markup=client_kb.about_us)
    await callback.message.delete_reply_markup()

@router.callback_query(F.data=='back2')
async def back2 (callback:CallbackQuery):
    await callback.message.answer('Hi!. Welcome to the IT park of the bot',reply_markup=client_kb.start_up) 
    await callback.message.delete_reply_markup()
@router.callback_query(F.data=='aboutus')
async def about_command(callback:CallbackQuery):
    cancel=InlineKeyboardBuilder()
    cancel.add(InlineKeyboardButton(text='back',callback_data='back1'))
    about_info=[]
    data=await client_info.show_about()
    for i in data:
        about_info.append(re.sub("[(),'']",'',str(i)))
    await bot.send_message(chat_id=callback.from_user.id,text=f"{about_info[0]}",reply_markup=cancel.as_markup())
    await callback.message.delete_reply_markup()

@router.callback_query(F.data=='back1')
async def back1(callback:CallbackQuery):
    await callback.message.answer('You can find out about us here',reply_markup=client_kb.about_us)
    await callback.message.delete_reply_markup()

@router.callback_query(F.data=='ourcourses')
async def about_courses(callback:CallbackQuery):
    await callback.message.answer('List of courses we have available',reply_markup=client_kb.client_group)   

@router.callback_query(F.data=='python_info')
@router.callback_query(F.data=='php_info')
@router.callback_query(F.data=='html_info')
@router.callback_query(F.data=='flutter_info')
async def language_coding(callback:CallbackQuery):
    if callback.data=='python_info':
        python1=[]   
        await callback.message.answer('You can read information about Python')
        data= await client_info.python_info(callback)
        print(callback.data)
        for i in data:
            python1.append(re.sub("[(),'']",'',str(i)))
            print(i) 
        await callback.message.answer(text=f'{python1}')

        
        #await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations'),BotCommand(command='status',description='your monthly payments and cashback'),BotCommand(command='lesson', description='List of lessons'),BotCommand(command='courses',description='List of courses'),BotCommand(command='settings',description='Bot settings')],BotCommandScopeChat(chat_id=data['user_id']))
 #       await client_info.add_user_info(callback,state)
#        await state.clear()       
#    if callback.data=='php':
#        data= await state.update_data(prg_languages='php')
#        await state.set_state(Form.user_id)
#        await callback.answer('You have registed',show_alert=True)
#        await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations'),BotCommand(command='status',description='your monthly payments and cashback'),BotCommand(command='lesson', description='List of lessons'),BotCommand(command='courses',description='List of courses'),BotCommand(command='settings',description='Bot settings')],BotCommandScopeChat(chat_id=data['user_id']))  
#        await client_info.add_user_info(callback,state)
#        await state.clear()
#    if callback.data=='htmlcss':
#        data=await state.update_data(prg_languages='htmlcss')
#        await state.set_state(Form.user_id)
#        await callback.answer('You have registed',show_alert=True)
#        await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations'),BotCommand(command='status',description='your monthly payments and cashback'),BotCommand(command='lesson', description='List of lessons'),BotCommand(command='courses',description='List of courses'),BotCommand(command='settings',description='Bot settings')],BotCommandScopeChat(chat_id=data['user_id']))  
#        await client_info.add_user_info(callback,state)
#        await state.clear()
#    await callback.message.delete_reply_markup()
#
#








    


        
   
   
    
    
    

   

