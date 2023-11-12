from aiogram import F,Router
from aiogram.types import Message,CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder,InlineKeyboardButton   
from aiogram.filters import Command, CommandStart, Filter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from aiogram.utils.formatting import Text
from keyboard import admin_kb
from database import admin_info


router_admin=Router()

pass_update=None


class Update_path(StatesGroup):
    new_path=State()





@router_admin.message(Command('admin'))
@router_admin.message(F.text.lower()=='admin')
async def admin_window_open(message:Message):
    global pass_update
    await message.answer(f'Welcome {message.from_user.full_name}')
    path=('12345',)
    await admin_info.old_pass(path)
    await message.answer('Please enter your passport')
    await message.delete()
    pass_update=admin_info.get_pass()
    print(pass_update)
   

@router_admin.message(F.text=='12345')
async def check_password(message:Message):
        await message.answer(text='you answered correctly',reply_markup=admin_kb.admin_window_kb)
        await message.delete()
    #else:
    #    await message.answer(text='You answered wrong')
    #    return  await admin_window_open(message)



@router_admin.message(Command('Settings'))
@router_admin.message(F.text.lower()=='settings')
async def settings_admin(message:Message):
    await message.answer(text='Admin Settings',reply_markup=admin_kb.admin_settings_kb)


@router_admin.message(F.text.lower()=='update password')
#@router_admin.message(F.text.endswith(''))
async def show_path(message:Message):
    update_builder=InlineKeyboardBuilder()
    update_builder.row(InlineKeyboardButton(text='Update',callback_data='Update'))
    await message.answer(text=f"{message.text.capitalize()}")
    await admin_info.show_path(message,update_builder) 

@router_admin.callback_query()
async def update_path(callback:CallbackQuery,state:FSMContext):
    if callback.data=='Update':
        await callback.answer('Please input new password')
        await state.set_state(Update_path.new_path)

@router_admin.message(Update_path.new_path)
async def update_path2(message:Message, state:FSMContext):
    save_builder=InlineKeyboardBuilder()
    save_builder.row(InlineKeyboardButton(text='Save',callback_data='Save'))
    await state.update_data(new_path=message.text)
    await message.delete()
    data= await state.get_data()
    if data['new_path']!='':
        await message.answer(f"Your new password {data['new_path']}",reply_markup=save_builder.as_markup())
        await admin_info.update_pass(message,state)
        await state.clear()
       