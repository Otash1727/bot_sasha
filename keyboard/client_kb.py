from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove,InlineKeyboardButton,InlineKeyboardMarkup)



contact_markup=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Share your contact with us', request_contact=True)]
    ],
    input_field_placeholder='Must input your phone number',
    resize_keyboard=True,
    selective=True,

)

contact_remove=ReplyKeyboardRemove(remove_keyboard=True)


client_profile_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Profile', callback_data='profile'),
            InlineKeyboardButton(text="Status", callback_data='status'),
            InlineKeyboardButton(text="Referral",callback_data='referral')
        ],
        [
            InlineKeyboardButton(text="Courses", callback_data='courses'),
            InlineKeyboardButton(text="Lessons", callback_data='lessons'),
            InlineKeyboardButton(text="Settings", callback_data='setting')
        ]
    ],
   
)



client_group=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Python',callback_data='python')
        ],
        [
            InlineKeyboardButton(text='Php',callback_data='php')
        ],
        [
            InlineKeyboardButton(text='Html Css', callback_data='htmlcss')
        ]
    ]
)