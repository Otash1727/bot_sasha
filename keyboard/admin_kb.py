from aiogram.types import (ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup)

""" admin commands:
        /find
        /create
        /transactions
        /list of groups, courses, teachers, students, 
        /group
        /settings        
"""

admin_window_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=' 🔍 Search in all catigories', callback_data='find')]
            ,
        [
            InlineKeyboardButton(text='Add informations ',callback_data='schoolinfo'),
            InlineKeyboardButton(text='Transactions',callback_data='transaction')
        ],
        [
         #   InlineKeyboardButton(text='Create',callback_data='create'),
            InlineKeyboardButton(text='Group',callback_data='group'),
            InlineKeyboardButton(text='Settings',callback_data='settings'),
        ]
    ]   
)

show_group_list=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Members of group',callback_data='members'),
            InlineKeyboardButton(text='List of group')
        ]
    ]
)

add_info_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Marking the role', callback_data='Mrole'),
            InlineKeyboardButton(text='List of payments',callback_data='Lpayments')
        ],
        [
            InlineKeyboardButton(text='List of partners',callback_data='partners'),
            InlineKeyboardButton(text='Cashback',callback_data='cashback')
        ]
    ]
)
list_group=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Python',callback_data='python_group')
        ],
        [
            InlineKeyboardButton(text="HTML CSS",callback_data='htmlcss_group')
        ],
        [
            InlineKeyboardButton(text='PHP',callback_data='php_group')
        ]
    ]
)

