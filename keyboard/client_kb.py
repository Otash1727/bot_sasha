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

about_us=InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='About us',callback_data='about_us'),
        InlineKeyboardButton(text='Our courses',callback_data='ourcourses')
        ],
        [
          InlineKeyboardButton(text='back',callback_data='back2') 
        ]
    ])
start_up=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Skip >>',callback_data='skip')
        ]
    ]
)

