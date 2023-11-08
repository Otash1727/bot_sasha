from create_bot import bot,dp,router
from aiogram import Dispatcher,types
from aiogram.types import Message,BotCommand,BotCommandScope,Update
from aiogram.filters import Command

dp.message(Command('start'))
async def start(message:types.Message):
    if message.text=='/start':
        await message.reply('welcome')












