from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder,InlineKeyboardButton,KeyboardBuilder,InlineKeyboardMarkup 
from aiogram.types import Message,BotCommand,BotCommandScopeChat,CallbackQuery,BotCommandScopeDefault,InlineQuery,InlineQueryResultArticle,InputTextMessageContent,InlineQueryResultPhoto
from database import client_info,courses_info
from aiogram import F,Router
from aiogram.enums import ParseMode
import re
from create_bot import bot,dp
from Photos import *

router=Router()

""" profile inline_query """

@router.inline_query(F.query.startswith('profile'))
async def profile_query(query:InlineQuery):
    tg=[]   
    check=await client_info.show_user_id()
    for i in check:
        tg.append(re.sub("[(),'']",'',str(i)))
    if str(query.from_user.id) in str(tg):
        data=await client_info.profile_query(query)    
        results=[InlineQueryResultArticle(description=f"{i[0]}",title="Personal information",id=(f"{i[3]}"),input_message_content=InputTextMessageContent(message_text=f"<b>Full name - <i>{i[0].upper()}</i>\nPhone number - <i>{i[1]}</i>\nActive cources - <i>{i[2]}</i>\nRole - <i>{i[4]}</i>\nExtra role - <i>{i[5]}</i>\nMonthly payment - <i>{i[6]}</i>\nInvite people - <i>{i[7]}</i>  </b>",parse_mode=ParseMode.HTML))for i in data]
        await query.answer(results=results)
        print(1)
    else:
        await query.answer(results=[InlineQueryResultArticle(description='Not found information',title=f"{query.from_user.full_name}",id=str(query.from_user.id),input_message_content=InputTextMessageContent(message_text='<b>404\n Not found</b>',parse_mode=ParseMode.HTML))])
    
""" courses inline_query"""
@router.inline_query(F.query.startswith('#'))
async def switch_courses(query:InlineQuery):
    print(query.query.split('#'), query.chat_type)
    data= await courses_info.queryById(query)
    results=[InlineQueryResultArticle(description=f"{dataes[3]}", title=f"{dataes[1]}", id=f'{dataes[0]}',input_message_content= InputTextMessageContent(message_text=f"<i><b> <a href='{dataes[3]}'>{dataes[1].upper()}</a>\nDescription:{dataes[2].upper()}</b></i>\n<b>img</b>\n<b>Price:{dataes[4]}</b>",parse_mode=ParseMode.HTML))for dataes in data]
    await query.answer(results=results)

@router.inline_query(F.query=='courses')
async def all_courses(query:InlineQuery):
    data= await courses_info.show_courses()
    results=[InlineQueryResultArticle(description=f"{dataes[3]}", title=f"{dataes[1]}", id=f'{dataes[0]}',input_message_content= InputTextMessageContent(message_text=f"<i><b> <a href='{dataes[3]}'>{dataes[1].upper()}</a>\nDescription:{dataes[2].upper()}</b></i>\n<b>img</b>\n<b>Price:{dataes[4]}</b>",parse_mode=ParseMode.HTML))for dataes in data]
    await query.answer(results=results)
    await gg.ddd()

"""accounting inline_query"""
#@router.inline_query(F.query.startswith('account'))
#async def account_query(query:InlineQuery):
#    tg=[]   
#    check=await client_info.show_user_id()
#    for i in check:
#        tg.append(re.sub("[(),'']",'',str(i)))
#    if str(query.from_user.id) in str(tg):
#        data=await client_info.accounting_query(query)
#        url="https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.geeksforgeeks.org%2Fwp-content%2Fcdn-uploads%2F20220602110655%2FAccounting-banner.png&tbnid=oe6wATVsXQl4iM&vet=12ahUKEwigiqGgi4iDAxWIIBAIHTXRDwkQMygWegUIARCBAQ..i&imgrefurl=https%3A%2F%2Fwww.geeksforgeeks.org%2Fintroduction-to-accounting%2F&docid=vHYktiKtNUGOLM&w=1000&h=500&q=accounting%20image&ved=2ahUKEwigiqGgi4iDAxWIIBAIHTXRDwkQMygWegUIARCBAQ"
#        results=[InlineQueryResultPhoto(photo_url=f"{url}",thumbnail_url=url,description='ss',id='ssss')]
#        await query.answer(results,is_personal=True)