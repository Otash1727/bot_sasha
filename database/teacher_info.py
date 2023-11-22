import sqlite3 as sq
from create_bot import bot
from database import client_info

async def check_teacher(message):
    client_info.cur.execute("Select * FROM info_users")
    show=client_info.cur.fetchall()
    return show