from aiogram.types import (ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton)

""" admin commands:
        /find
        /create
        /transactions
        /list of groups, courses, teachers, students, 
        /group
        /settings        
"""

admin_window_kb=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Find'),
            KeyboardButton(text='Create'),
            KeyboardButton(text='Transactions')
        ],
        [
            KeyboardButton(text='School informations '),
            KeyboardButton(text='Group'),
            KeyboardButton(text='Settings'),
        ]
    ],
    selective=True,
    resize_keyboard=True
)


admin_settings_kb=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Update password'),
            KeyboardButton(text='Change the language')
        ],
        [
            KeyboardButton(text='back')
        ]
    ],
    resize_keyboard=True,
    selective=True
)