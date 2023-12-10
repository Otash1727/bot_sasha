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

#id,name,description,images
"""General functation"""

async def show_courses():
    client_info.cur.execute("SELECT * FROM info_courses")
    show_course=client_info.cur.fetchall()
    return show_course

async def findById(callback):
    data= callback.data.split(':')
    client_info.cur.execute("SELECT * FROM info_courses WHERE id=?",data[1],)
    show_languages=client_info.cur.fetchall()
    return show_languages

async def queryById(query):
    data=query.query.split('#')
    one=(data[1],)
    print(one)
    client_info.cur.execute("SELECT * FROM info_courses WHERE name=?",one,)
    show_query=client_info.cur.fetchall()
    return  show_query

async def show_about():
    client_info.cur.execute("SELECT about_us FROM info_users WHERE user_id=1")
    about=client_info.cur.fetchall()
    return about