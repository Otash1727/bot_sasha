from aiogram.types import (ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup)

""" admin commands:
        /find
        /create
        /transactions
        /list of groups, courses, teachers, students, 
        /group
        /settings        
"""
# is_active bool 0

admin_window_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=' 🔍 Search in all catigories', switch_inline_query_current_chat='')
        ]
        ,
        [
            InlineKeyboardButton(text=' Users ',switch_inline_query_current_chat='$')],
        [
            InlineKeyboardButton(text=' Courses ',switch_inline_query_current_chat='#')
        ],
        [
         #   InlineKeyboardButton(text='Create',callback_data='create'),
            InlineKeyboardButton(text=' Group ',switch_inline_query_current_chat='@')
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

transaction_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Search by Group',callback_data='by_group')
        ],
        [
            InlineKeyboardButton(text='Search by other catigories',callback_data='other_catigories')
        ]
    ]
)

