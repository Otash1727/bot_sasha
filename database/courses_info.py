import sqlite3 as sq
from database import client_info


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


"""General functation"""

async def show_courses():
    client_info.cur.execute(f"SELECT * FROM info_courses")
    show_languages=client_info.cur.fetchall()
    return show_languages

async def show_about():
    client_info.cur.execute("SELECT about_us FROM info_users WHERE user_id=1")
    about=client_info.cur.fetchall()
    return about