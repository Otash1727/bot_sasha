from aiogram import F,Router
from aiogram.types import Message,CallbackQuery,KeyboardButton,ReplyKeyboardMarkup,Message,BotCommand,BotCommandScopeChat,CallbackQuery,BotCommandScopeDefault
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder,InlineKeyboardButton,KeyboardBuilder 
from aiogram.methods.delete_my_commands import DeleteMyCommands  
from aiogram.filters import Command, CommandStart, Filter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from database import teacher_info
"""
teacher commands:
        /create
        /settings
        /balance
        /profile
        /settings        
"""

router_teacher=Router()


@router_teacher.message(Command('teacher'))
async def start_teacher(message:Message):
    data= await teacher_info.check_teacher(message=message)
    await message.answer('123')
    for i in data:
        print(i)


