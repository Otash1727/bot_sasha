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

get_phone_number=None
class Info(StatesGroup):
    name=State()
    phone=State()


@router.message(Command('start'))
async def cdm_start(message:Message):
    await message.answer('Hi there. What\'s your name', reply_markup=client_kb.contact_markup)





@router.message()
async def students_commands(message:Message):
    global get_phone_number
    get_phone_number=message.contact
    if get_phone_number!= None:
        await message.answer(text="Okey", reply_markup=client_kb.client_profile_kb)
    else:
        message.answer('Mistake')


@router.message(Text(equals='Referendum',ignore_case=True))
async def Ref_click(message:Message):
    await message.answer("Do'stlaringizni taklif qiling")
