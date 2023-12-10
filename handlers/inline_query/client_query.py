from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder,InlineKeyboardButton,KeyboardBuilder,InlineKeyboardMarkup 
from aiogram.types import Message,BotCommand,BotCommandScopeChat,CallbackQuery,BotCommandScopeDefault,InlineQuery,InlineQueryResultArticle,InputTextMessageContent
from database import client_info,courses_info
from aiogram import F,Router
from aiogram.enums import ParseMode

router=Router()

""" profile inline_query """

@router.inline_query(F.query.startswith('pro'))
async def profile_query(query:InlineQuery):
    check=await client_info.show_user_id()
    data=await client_info.profile_query(query)    
    results=[InlineQueryResultArticle(description=f"{i[0]}",title="Personal information",id=f"{i[3]}",input_message_content=InputTextMessageContent(message_text=f"<b>Full name - <i>{i[0].upper()}</i>\nPhone number - <i>{i[1]}</i>\nActive cources - <i>{i[2]}</i>\nRole - <i>{i[4]}</i>\nExtra role - <i>{i[5]}</i>\nMonthly payment - <i>{i[6]}</i>\nInvite people - <i>{i[7]}</i>  </b>",parse_mode=ParseMode.HTML))for i in data]
    await query.answer(results=results)
    print(query.query)
    
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
