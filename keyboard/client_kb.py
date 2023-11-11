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
            KeyboardButton(text='Profile'),
            KeyboardButton(text="Status"),
            KeyboardButton(text="Referral")
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

client_group=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='PYTHON'),
            KeyboardButton(text="PHP"),
            KeyboardButton(text="HTML CSS")
        ]
    ],
    resize_keyboard=True,
    selective=True,
    input_field_placeholder="which programming languages do you want to choose"
)