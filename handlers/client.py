from aiogram import Router , F
from aiogram.types import Message
from aiogram.utils.formatting import Text, Bold
from aiogram.filters import Command, CommandStart
from aiogram.enums.content_type import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboard import client_kb
import logging


router=Router()


class Form(StatesGroup):
    name=State()
   


@router.message(Command('start'))
async def cdm_start(message:Message,state:FSMContext):
    await state.set_state(Form.name)
    await message.answer('Hi there. What\'s your name')

@router.message(Form.name)
async def contact_number(message:Message, state:FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Thnaks',reply_markup=client_kb.contact_markup)
    data= await state.get_data()
    for i in data.items():
        print(i)
    await state.clear()
    
    
    

   

