from os import getenv
from aiogram import Dispatcher,Bot
from dotenv import load_dotenv


load_dotenv()
token = getenv('token')
bot=Bot(token)
dp=Dispatcher()