from aiogram import Router ,F
from aiogram.utils.deep_linking import decode_payload,create_deep_link
from aiogram.types import Message,BotCommand,BotCommandScopeChat,CallbackQuery,BotCommandScopeDefault
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


router=Router()


class Form(StatesGroup):
    name=State()
    sur_name=State()
    phone=State()
    user_id=State()
    prg_languages=State()
    

   
@router.message(Command('start'))
async def cdm_start(message:Message):
    await client_info.show_user_id(message)
    


@router.message(Command('register'))
async def register_command(message:Message,state:FSMContext):
    await message.answer('Hello you want to register our bot. Please input your name')
    await state.set_state(Form.name)


@router.message(Form.name)
async def input_name(message:Message, state:FSMContext):
    await state.update_data(name=message.text.lower())
    await state.update_data(user_id=message.from_user.id)
    await message.answer("Please input your surname")
    await state.set_state(Form.sur_name)
    
@router.message(Form.sur_name)
async def input_surname(message:Message,state:FSMContext):
    data=await state.update_data(sur_name=message.text.lower())    
    await message.answer(f"Okey now you need to send your phone number", reply_markup=client_kb.contact_markup)
    await state.set_state(Form.phone)
@router.message(Form.phone)
async def input_phone(message:Message,state:FSMContext):
    data=await state.update_data(phone=message.contact.phone_number)
    print(data['user_id'],data['phone'])
    if data['phone']!=None:
        await bot.send_message(chat_id=message.from_user.id,text='Thanks',reply_markup=client_kb.contact_remove)
        await state.set_state(Form.prg_languages) 
        await message.answer('Which programming languages do you want to learn. \n Please select', reply_markup=client_kb.client_group)



@router.callback_query(F.data=='python',Form.prg_languages)
@router.callback_query(F.data=='php',Form.prg_languages)
@router.callback_query(F.data=='htmlcss',Form.prg_languages)
async def language_coding(callback:CallbackQuery, state:FSMContext):
    if callback.data=='python':
        data=await state.update_data(prg_languages='python')
        await state.set_state(Form.user_id)
        await callback.answer('You have registed',show_alert=True)
        await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations'),BotCommand(command='status',description='your monthly payments and cashback'),BotCommand(command='lesson', description='List of lessons'),BotCommand(command='courses',description='List of courses'),BotCommand(command='settings',description='Bot settings')],BotCommandScopeChat(chat_id=data['user_id']))
        await client_info.add_user_info(callback,state)
        await state.clear()       
    if callback.data=='php':
        data= await state.update_data(prg_languages='php')
        await state.set_state(Form.user_id)
        await callback.answer('You have registed',show_alert=True)
        await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations'),BotCommand(command='status',description='your monthly payments and cashback'),BotCommand(command='lesson', description='List of lessons'),BotCommand(command='courses',description='List of courses'),BotCommand(command='settings',description='Bot settings')],BotCommandScopeChat(chat_id=data['user_id']))  
        await client_info.add_user_info(callback,state)
        await state.clear()
    if callback.data=='htmlcss':
        data=await state.update_data(prg_languages='htmlcss')
        await state.set_state(Form.user_id)
        await callback.answer('You have registed',show_alert=True)
        await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations'),BotCommand(command='status',description='your monthly payments and cashback'),BotCommand(command='lesson', description='List of lessons'),BotCommand(command='courses',description='List of courses'),BotCommand(command='settings',description='Bot settings')],BotCommandScopeChat(chat_id=data['user_id']))  
        await client_info.add_user_info(callback,state)
        await state.clear()
    await callback.message.delete_reply_markup()











    


        
   
   
    
    
    

   

