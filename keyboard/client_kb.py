from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove)



contact_markup=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Please send your phone number', request_contact=True)]
    ],
    input_field_placeholder='Must input your phone number',
    resize_keyboard=True,
    selective=True
)


client_profile_kb=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Referendum'),
            KeyboardButton(text="Status"),
            KeyboardButton(text="Profile")
        ],
        [
            KeyboardButton(text="Courses"),
            KeyboardButton(text="Lessons"),
            KeyboardButton(text="Settings")
        ]
    ],
    resize_keyboard=True,
    selective=True
)