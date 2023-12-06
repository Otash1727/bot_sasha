from aiogram import Router ,F
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder,InlineKeyboardButton,KeyboardBuilder 
from aiogram.utils.deep_linking import decode_payload,create_deep_link
from aiogram.types import Message,BotCommand,BotCommandScopeChat,CallbackQuery,BotCommandScopeDefault,InlineQuery,InlineQueryResultArticle
from aiogram.methods.delete_my_commands import DeleteMyCommands
from aiogram.utils.formatting import Text, Bold
from aiogram.filters import Command, CommandStart, Filter
from aiogram.enums.content_type import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboard import client_kb
from database import client_info,languages_info
import logging
import time
from create_bot import bot 
import re


router=Router()


class Form(StatesGroup):
    name=State()
    phone=State()
    user_id=State()
    #prg_languages=State()
    

   
@router.message(Command('start'))
async def cdm_start(message:Message,state:FSMContext):
    tg_id=[]
    data= await client_info.show_user_id()
    for i in data:
        tg_id.append(re.sub("[(),'']",'',str(i)))
    if str(message.from_user.id) in str(tg_id):
        await message.answer('You have already registered from our bot \n Please select the commands to use the bot')
        await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations'),BotCommand(command='accounting',description='your balance and cashback, monthly payments'),BotCommand(command='lesson', description='List of lessons'),BotCommand(command='courses',description='List of courses'),BotCommand(command='settings',description='Bot settings'),BotCommand(command='cancel',description='cancel the current operation'),BotCommand(command='help',description='help')],BotCommandScopeChat(chat_id=message.from_user.id))
    else:
        await message.answer('Hi!. Welcome to the IT park of the bot\n Input your name',reply_markup=client_kb.start_up)
        await state.set_state(Form.name)


@router.message(Command('help'))
async def command_help(message:Message):
    await bot.send_message(chat_id=message.from_user.id, text="<i><b>The list of commands to use the bot for you</b></i> \n \n /start - <b>run the bot</b>\n \n /profile -<b> User's information</b>\n \n /accounting - <b>your balance and cashback,monthly paymets</b>\n \n /courses -<b> about list of our courses</b>\n \n /lesson - <b>your lessons and homeworks</b>\n \n /settings - <b>options of the bot</b> ",parse_mode=ParseMode.HTML)     

@router.message(Form.name)
async def input_name(message:Message, state:FSMContext):
    await state.update_data(name=message.text.lower())
    await state.update_data(user_id=message.from_user.id)
    await message.answer(text='Thanks',reply_markup=client_kb.contact_markup)
    await message.answer(f"Okey now you need to send your phone number with button or write message \n For example: +998.........", reply_markup=client_kb.start_up)
    await state.set_state(Form.phone)

def textToPhoneValidate(message: Message):
    return message.contact is not None or (message.text.startswith('+') and len(message.text) ==13);

@router.message(Form.phone)
async def input_phone(message:Message,state:FSMContext):
    if not textToPhoneValidate(message):
        return await message.answer('You wrong to input your phone number \n For example: +998.........',reply_markup=client_kb.start_up)
    phoneNumber = message.contact.phone_number if message.contact is not None else message.text
    data = await state.update_data(phone=phoneNumber)
    print(data['user_id'],data['phone'])
    sendedMessage =  await bot.send_message(chat_id=message.from_user.id,text='Thanks',reply_markup=client_kb.contact_remove)
    await client_info.add_user_info(state)
    await state.clear() 
    answeredMessage = await message.answer('You have registed \n Please select the commands to use the bot')
    #time.sleep(2);
    #await sendedMessage.delete();
    await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations'),BotCommand(command='accounting',description='your balance and cashback, monthly payments'),BotCommand(command='lesson', description='List of lessons'),BotCommand(command='courses',description='List of courses'),BotCommand(command='settings',description='Bot settings'),BotCommand(command='cancel',description='cancel the current operation'),BotCommand(command='help',description='help')],BotCommandScopeChat(chat_id=message.from_user.id))
    await bot.send_message(chat_id=message.from_user.id, text="<i><b>The list of commands to use the bot for you</b></i> \n \n /start - <b>run the bot</b>\n \n /profile -<b> User's information</b>\n \n /accounting - <b>your balance and cashback,monthly paymets</b>\n \n /courses -<b> about list of our courses</b>\n \n /lesson - <b>your lessons and homeworks</b>\n \n /settings - <b>options of the bot</b> ",parse_mode=ParseMode.HTML)
   
"""SKIP FUNCTATION  """

@router.callback_query(F.data=='skip')
async def skip_command(callback:CallbackQuery,state:FSMContext):
    await state.clear()
    await callback.message.edit_text('You can find out about us here',reply_markup=client_kb.about_us)
    #await callback.message.delete_reply_markup()


@router.callback_query(F.data=='back2')
async def back2 (callback:CallbackQuery,state:FSMContext):
        await callback.message.edit_text('Hi!. Welcome to the IT park of the bot\n Input your name',reply_markup=client_kb.start_up)
        await state.set_state(Form.name)

@router.callback_query(F.data=='about_us')
async def about_command(callback:CallbackQuery):
    cancel=InlineKeyboardBuilder()
    cancel.add(InlineKeyboardButton(text='back',callback_data='back1'))
    about_info=[]
    data=await languages_info.show_courses(callback=callback)
    for i in data:
        about_info.append(re.sub("[(),'']",'',str(i)))
    print(about_info)
    if len(about_info) != 0:
        await callback.message.edit_text(text=f"{about_info}",reply_markup=cancel.as_markup());
        # await callback.message.edit_reply_markup()
    else:
        await callback.message.edit_text(text="Not found informations",reply_markup=cancel.as_markup());
        # await bot.send_message(chat_id=callback.from_user.id,text="Not found informations")
    #await callback.message.delete_reply_markup()

@router.callback_query(F.data=='back1')
async def back1(callback:CallbackQuery):
    await callback.message.edit_text('You can find out about us here',reply_markup=client_kb.about_us)

@router.callback_query(F.data=='back3')
async def back1(callback:CallbackQuery):
    data=await client_info.show_user_id()
    if len(data)==0: 
        return await callback.message.edit_text('You can find out about us here',reply_markup=client_kb.about_us)
    for i in data:
        i
    if callback.from_user.id in i:
        await callback.message.edit_text(text="<i><b>The list of commands to use the bot for you</b></i> \n \n /start - <b>run the bot</b>\n \n /profile -<b> User's information</b>\n \n /accounting - <b>your balance and cashback,monthly paymets</b>\n \n /courses -<b> about list of our courses</b>\n \n /lesson - <b>your lessons and homeworks</b>\n \n /settings - <b>options of the bot</b> ",parse_mode=ParseMode.HTML)
    
    #await callback.message.delete_reply_markup()

@router.callback_query(F.data=='ourcourses')
async def about_courses(callback:CallbackQuery):
    await callback.message.edit_text('List of courses we have available',reply_markup=client_kb.client_group) 



@router.callback_query(F.data=='python_info')
@router.callback_query(F.data=='php_info')
@router.callback_query(F.data=='htmlcss_info')
@router.callback_query(F.data=='flutter_info')
async def language_coding(callback:CallbackQuery):
    cancel2=InlineKeyboardBuilder()
    cancel2.add(InlineKeyboardButton(text='back',callback_data='back4'))
    data1= await languages_info.show_courses(callback)
    if  len(data1)==0 and (callback.data=='python_info'or callback.data=='php_info' or callback.data=='htmlcss_info'or callback.data=='flutter_info'):
        return  await callback.message.answer('Not found information',reply_markup=cancel2.as_markup())
    for i in data1:
        (re.sub("[,()'']",'',str(i)))
    await callback.message.answer(text=f"{data1}",reply_markup=cancel2.as_markup())

    #        python1.append(re.sub("[(),'']",'',str(i)))
    #await callback.message.answer(text=f'1',reply_markup=cancel2.as_markup())
    #if callback.data=='python_info':
    #    python1=[]   
    #    await callback.message.answer('You can read information about Python')
    #    data= await languages_info.show_courses(callback=callback)
    #    print(callback.data)
    #    for i in data:
    #        python1.append(re.sub("[(),'']",'',str(i)))
    #    if python1!=[]: 
    #        await callback.message.answer(text=f'{python1}',reply_markup=cancel2.as_markup())
    #    else:
    #        await callback.message.answer('Not found information',reply_markup=cancel2.as_markup())
    #if callback.data=='php_info':
    #    php1=[]
    #    await callback.message.answer('You can read information about Python')
    #    data= await languages_info.show_courses(callback=callback)
    #    print(callback.data)
    #    for i in data:
    #        php1.append(i)
    #    if php1!=[]: 
    #        await callback.message.answer(text=f"{re.sub('[(),'']','',str(php1))}",reply_markup=cancel2.as_markup())
    #    else:
    #        await callback.message.answer('Not found information,reply_markup=cancel2.as_markup()')
    #if callback.data=='htmlcss_info':
    #    htmcss1=[]
    #    await callback.message.answer('You can read information about Python')
    #    data= await languages_info.show_courses(callback=callback)
    #    for i in data:
    #        htmcss1.append(i)
    #    if htmcss1!=[]: 
    #        await callback.message.answer(text=f'{htmcss1}',reply_markup=cancel2.as_markup())
    #    else:
    #        await callback.message.answer('Not found information',reply_markup=cancel2.as_markup())
    #if callback.data=='flutter_info':
    #    flutter1=[]
    #    await callback.message.answer('You can read information about Python')
    #    data= await languages_info.show_courses(callback=callback)
    #    print(callback.data)
    #    for i in data:
    #        htmcss1.append(re.sub("[(),'',[]]",'',str(i)))
    #    if htmcss1!=[]: 
    #        await callback.message.answer(text=f'{htmcss1}',reply_markup=cancel2.as_markup())
    #    else:
    #        await callback.message.answer('Not found information',reply_markup=cancel2.as_markup())
@router.callback_query(F.data=='back2')
async def back_2(callback:CallbackQuery):
    await callback.message.answer('You can find out about us here',reply_markup=client_kb.about_us)
@router.callback_query(F.data=='back4')
async def back_4(callback:CallbackQuery):
    data=await client_info.show_user_id()
    if len(data)==0: 
        return await callback.message.edit_text('You can find out about us here',reply_markup=client_kb.about_us)
    for i in data:
        i
    if callback.from_user.id in i:
        await callback.message.edit_text('List of courses we have available',reply_markup=client_kb.client_group) 


"""Commands functions"""

@router.message(Command('profile'))
async def profile_command(message:Message):
    data=await client_info.profile_funtions(message=message)
    for i in data:
        print(i)
    await message.answer(f"<b>Full name - <i>{i[0].upper()}</i>\nPhone number - <i>{i[1]}</i>\nActive cources - <i>{i[2]}</i>\nRole - <i>{i[4]}</i>\nExtra role - <i>{i[5]}</i>\nMonthly payment - <i>{i[6]}</i>\nInvite people - <i>{i[7]}</i>  </b>",parse_mode=ParseMode.HTML)

@router.message(Command('courses'))
async def show2_courses(message:Message):
    await message.answer ('List of courses we have available',reply_markup=client_kb.client_group)



        #await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations'),BotCommand(command='status',description='your monthly payments and cashback'),BotCommand(command='lesson', description='List of lessons'),BotCommand(command='courses',description='List of courses'),BotCommand(command='settings',description='Bot settings')],BotCommandScopeChat(chat_id=data['user_id']))
 #       await client_info.add_user_info(callback,state)
#        await state.clear()       
#    if callback.data=='php':
#        data= await state.update_data(prg_languages='php')
#        await state.set_state(Form.user_id)
#        await callback.answer('You have registed',show_alert=True)
#        await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations'),BotCommand(command='status',description='your monthly payments and cashback'),BotCommand(command='lesson', description='List of lessons'),BotCommand(command='courses',description='List of courses'),BotCommand(command='settings',description='Bot settings')],BotCommandScopeChat(chat_id=data['user_id']))  
#        await client_info.add_user_info(callback,state)
#        await state.clear()
#    if callback.data=='htmlcss':
#        data=await state.update_data(prg_languages='htmlcss')
#        await state.set_state(Form.user_id)
#        await callback.answer('You have registed',show_alert=True)
#        await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations'),BotCommand(command='status',description='your monthly payments and cashback'),BotCommand(command='lesson', description='List of lessons'),BotCommand(command='courses',description='List of courses'),BotCommand(command='settings',description='Bot settings')],BotCommandScopeChat(chat_id=data['user_id']))  
#        await client_info.add_user_info(callback,state)
#        await state.clear()
#    await callback.message.delete_reply_markup()
#
#


"""Empty handler"""
@router.message()
async def empty_handler(message:Message):
    await message.answer("I don't understand you")





    


        
   
   
    
    
    

   

