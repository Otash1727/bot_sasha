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
            InlineKeyboardButton(text='Python',callback_data='python_info'),
            InlineKeyboardButton(text='Php',callback_data='php_info')
        ],
        [
            InlineKeyboardButton(text='Html Css', callback_data='htmlcss_info'),
            InlineKeyboardButton(text='Flutter', callback_data='flutter_info')
        ],
        [
            InlineKeyboardButton(text='<<back',callback_data='back3')
        ]
    ]
)   


start_up=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Skip >>',callback_data='skip')
        ]
    ]
)
about_us=InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='About us',callback_data='about_us'),
        InlineKeyboardButton(text='Our courses',callback_data='ourcourses')
        ],
        [
          InlineKeyboardButton(text='<back',callback_data='back2') 
        ]
    ]
)