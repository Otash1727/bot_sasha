from aiogram import Router ,F
from aiogram.types import Message
from aiogram.utils.formatting import Text, Bold
from aiogram.filters import Command, CommandStart, Filter
from aiogram.enums.content_type import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboard import client_kb
import logging


router=Router()


class Form(StatesGroup):
    name=State()
    phone=State()
    IT_languages=State()
    user_id=State()

   


@router.message(Command('start'))
async def cdm_start(message:Message,state:FSMContext):
    await state.set_state(Form.name)
    await message.answer('Hi there. What\'s your name')

@router.message(Form.name)
async def name_users(message:Message, state:FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Thnaks',reply_markup=client_kb.contact_markup)
    await state.set_state(Form.phone)


@router.message(Form.phone)
async def contact_users(message:Message, state:FSMContext):
    await state.update_data(message.contact)
    await message.answer('Which programming languages do you want to learn', reply_markup=client_kb.client_group)
    await state.set_state(Form.IT_languages)


@router.message(F.text.lower()=='php', Form.IT_languages)
async def languages_users(message:Message,state:FSMContext):
    await state.update_data(IT_languages='PHP')
    await message.answer('It\'s a perfect choise')



        
   
   
    
    
    

   

