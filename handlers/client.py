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
    phone=State()
    prg_languages=State()
    user_id=State()

   
@router.message(Command('start'))
async def cdm_start(message:Message):
    await bot.set_my_commands([BotCommand(command='register',description='Register to use our bot')],BotCommandScopeChat(chat_id=message.from_user.id))
    await message.answer('Register to use our bot')
    


@router.message(Command('register'))
async def register_command(message:Message,state:FSMContext):
    await message.answer('Hello you want to register our bot. Please input your name')
    await state.set_state(Form.name)


@router.message(Form.name)
async def input_name(message:Message, state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.phone)
    await message.answer(f"Okey now you need to send your phone number", reply_markup=client_kb.contact_markup)

@router.message(Form.phone)
async def input_phone(message:Message,state:FSMContext):
    data=await state.update_data(phone=message.contact)
    if data['phone']!=None:
        await bot.send_message(chat_id=message.from_user.id,text='Thanks',reply_markup=client_kb.contact_remove)
        await state.set_state(Form.prg_languages) 
        await message.answer('Which programming languages do you want to learn. \n Please select', reply_markup=client_kb.client_group)



@router.callback_query(F.data=='python',Form.prg_languages)
@router.callback_query(F.data=='php',Form.prg_languages)
@router.callback_query(F.data=='htmlcss',Form.prg_languages)
async def language_coding(callback:CallbackQuery, state:FSMContext):
    if callback.data=='python':
        await state.update_data(prg_languages='python')
        await state.set_state(Form.user_id)
        await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations')],BotCommandScopeChat(chat_id=callback.message.from_user.id))       
    if callback.data=='php':
        await state.update_data(prg_languages='php')
        await state.set_state(Form.user_id)
    if callback.data=='htmlcss':
        await state.update_data(prg_languages='htmlcss')
        await state.set_state(Form.user_id)
    await callback.message.delete_reply_markup()

#@router.message(Form.user_id,Command('dd'))
#async def window_user(message:Message, state:FSMContext):
#    data=await state.update_data(user_id=message.from_user.id)
#    await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations')],BotCommandScopeChat#(chat_id=message.from_user.id))
#    await state.clear()
"""
@router.message(Command('cancel'))
async def cancel_client_state(message:Message,state:FSMContext):
    current_client_state= await state.get_data()
    if current_client_state == None:
        return
    await state.clear()
    await message.answer("You can start from the beginning.  Please input your name")


@router.message(F.text, Form.name)
async def users_name(message:Message,state:FSMContext):
    data=await state.update_data(name=message.text)
    await state.set_state(Form.phone)
    await message.answer(f"Okey now you need to send your phone number", reply_markup=client_kb.contact_markup)
    

@router.message(Form.phone)
async def users_phone(message:Message, state:FSMContext):
    data=await state.update_data(phone=message.contact.phone_number)
    await state.set_state(Form.prg_languages)
    if data['phone']!='':
        await message.answer("Good!. Which programming languages do you want to learn",reply_markup=client_kb.client_group)
        

@router.message(Form.prg_languages)
async def programming_languages(message:Message, state:FSMContext):
        if message.text.lower()=='php':
            await state.set_state(Form.user_id)
            await state.update_data(prg_languages=message.text)
            await message.answer("It's a pecrfetc choise")
            await message.answer('Your request is being processed ⏳')
            time.sleep(1.5)
            await message.answer(" You have registed",reply_markup=client_kb.client_profile_kb)
        elif message.text.lower()=='python':
            await state.set_state(Form.user_id)
            await state.update_data(prg_languages=message.text)
            await message.answer("it's a perfect choise")
            await message.answer('Your request is being processed ⏳')
            time.sleep(1.5)
            await message.answer(" You have registed",reply_markup=client_kb.client_profile_kb)
        elif message.text.lower()=='html css':
            await state.set_state(Form.user_id)
            await state.update_data(prg_languages=message.text)
            await message.answer(text="It's a perfect choise")
            await message.answer('Your request is being processed ⏳')
            time.sleep(1.5)
            await message.answer(" You have registed",reply_markup=client_kb.client_profile_kb)


@router.message(Form.user_id)
async def get_id(message:Message, state:FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await client_info.add_user_info(message, state)
    await state.clear()


# create deep link     
#@router.message(F.text=='Referral') 
#async def get_ref(message:Message):
   # link = await create_deep_link(str(message.from_user.username), encode=True,link_type='start')
  # result: 'https://t.me/MyBot?start='
  ## после знака = будет закодированный никнейм юзера, который создал реф ссылку, вместо него можно вставить и его id 
   # await message.answer(f"Ваша реф. ссылка {link}")
#    print(123)
"""                   







    


        
   
   
    
    
    

   

