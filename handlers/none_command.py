from aiogram import Router,F 
from aiogram.types import Message 
import logging


router2=Router()


@router2.message()
async def no_command(message:Message):
    await message.answer('You have made mistake')
