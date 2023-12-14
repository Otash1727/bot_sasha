import sqlite3 as sq
from database import client_info
from create_bot import bot
from aiogram.types import BotCommand,BotCommandScopeChat, CallbackQuery
import re
from aiogram.fsm.context import FSMContext
from keyboard import admin_kb


def sql_start():
    global db,cur, execute
    db=sq.connect("User_information.db")
    cur=db.cursor()
    def execute(string: str):
        try :
             
            return db.execute(string);
        except  Exception as error:
            print(error)
            return None;

"""Edit information users functation by admin"""
async def search_users(query):
    text=query.query.split('$')
    texts=text
    client_info.cur.execute(f"SELECT * FROM info_users WHERE name LIKE '{texts[1]}%' OR phone LIKE '{texts[1]}%' OR user_id LIKE '{texts[1]}%' OR role LIKE '{text[1]}%' OR extra_role LIKE '{texts[1]}%' OR payments LIKE '{texts[1]}%' OR invite_people LIKE '{texts[1]}%' OR cashback LIKE '{texts[1]}%' OR debt LIKE '{text[1]}%'")
    result=client_info.cur.fetchall()
    return result


"""Select column names"""
async def ff():
    column=client_info.cur.execute("SELECT * FROM info_users")
    return column