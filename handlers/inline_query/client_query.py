from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder,InlineKeyboardButton,KeyboardBuilder,InlineKeyboardMarkup 
from aiogram.types import Message,BotCommand,BotCommandScopeChat,CallbackQuery,BotCommandScopeDefault,InlineQuery,InlineQueryResultArticle,InputTextMessageContent,InlineQueryResultPhoto,InlineQueryResultCachedPhoto,FSInputFile
from database import client_info,courses_info
from aiogram import F,Router
from keyboard import *
from aiogram.enums import ParseMode
import re
from create_bot import bot,dp
from Photos import *

router=Router()

""" profile inline_query """

@router.inline_query(F.query.startswith('profile'))
async def profile_query(query:InlineQuery):
    logo='https://static.vecteezy.com/system/resources/thumbnails/002/318/271/small/user-profile-icon-free-vector.jpg'
    tg=[]   
    check=await client_info.show_user_id()
    for i in check:
        tg.append(re.sub("[(),'']",'',str(i)))
    if str(query.from_user.id) in str(tg):
        data=await client_info.profile_query(query)    
        results=[InlineQueryResultArticle(description=f"{i[0]}",title="Personal information",id=(f"{i[3]}"),thumbnail_url=logo,thumbnail_height=1,thumbnail_width=1,input_message_content=InputTextMessageContent(message_text=f"<b>Full name - <i>{i[0].upper()}</i>\nPhone number - <i>{i[1]}</i>\nActive cources - <i>{i[2]}</i>\nRole - <i>{i[4]}</i>\nExtra role - <i>{i[5]}</i>\nMonthly payment - <i>{i[6]}</i>\nInvite people - <i>{i[7]}</i>  </b>",parse_mode=ParseMode.HTML))for i in data]
        await query.answer(results=results)
        print(1)
    else:
        await query.answer(results=[InlineQueryResultArticle(description='Not found information',title=f"{query.from_user.full_name}",id=str(query.from_user.id),input_message_content=InputTextMessageContent(message_text='<b>404\n Not found</b>',parse_mode=ParseMode.HTML))])
    
""" courses inline_query"""
@router.inline_query(F.query.startswith('#'))
async def switch_courses(query:InlineQuery):
    print(query.query.split('#'), query.chat_type)
    data= await courses_info.queryById(query)
    results=[InlineQueryResultArticle(description=f"{dataes[2]}", title=f"{dataes[1]}", id=f'{dataes[0]}',thumbnail_url=dataes[5],thumbnail_height=1,thumbnail_width=1,input_message_content= InputTextMessageContent(message_text=f"<i><b> <a href='{dataes[3]}'>{dataes[1].upper()}</a>\nDescription:{dataes[2].upper()}</b></i>\n<b>Price:{dataes[4]}</b>",parse_mode=ParseMode.HTML))for dataes in data]
    await query.answer(results=results)
    print(data)

@router.inline_query(F.query=='courses')
async def all_courses(query:InlineQuery):
    data= await courses_info.show_courses()
    results=[InlineQueryResultArticle(description=f"{dataes[2]}", title=f"{dataes[1]}", id=f'{dataes[0]}',thumbnail_url=dataes[5],thumbnail_height=1,thumbnail_width=1,input_message_content= InputTextMessageContent(message_text=f"<i><b> <a href='{dataes[3]}'>{dataes[1].upper()}</a>\nDescription:{dataes[2].upper()}</b></i>\n<b>Price:{dataes[4]}</b>",parse_mode=ParseMode.HTML))for dataes in data]
    await query.answer(results=results,is_personal=True,cache_time=60)
    

"""accounting inline_query"""
@router.inline_query(F.query.startswith('account'))
async def account_query(query:InlineQuery):
    tg=[]   
    check=await client_info.show_user_id()
    for i in check:
        tg.append(re.sub("[(),'']",'',str(i)))
    if str(query.from_user.id) in str(tg):
        data=await client_info.accounting_query(query)
        image_url='https://cdn-icons-png.flaticon.com/512/5231/5231813.png'
        results=[InlineQueryResultArticle(title=f"{query.from_user.full_name.capitalize()}",description='Accounting information',thumbnail_url=image_url,thumbnail_height=1,thumbnail_width=1,id=query.query,input_message_content=InputTextMessageContent(message_text=f"Your monthly payments: <b><i>{dataes[0]}</i></b>\nPeople you invited: <b><i>{dataes[1]}</i></b>\nYour cashback: <b><i>{dataes[2]}</i></b>\nYour debt: <b><i>{dataes[3]}</i></b>",parse_mode=ParseMode.HTML))for dataes in data]
        await query.answer(results,is_personal=True,cache_time=60)
    else:
        await query.answer(results=[InlineQueryResultArticle(description='Not found information',title=f"{query.from_user.full_name}",id=str(query.from_user.id),input_message_content=InputTextMessageContent(message_text='<b>404\n Not found</b>',parse_mode=ParseMode.HTML))])
    