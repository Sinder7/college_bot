from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboards = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Расписание на сегодня'),
    
        KeyboardButton(text='Расписание на неделю')
    ],
    [
        KeyboardButton(text='Расписание на завтра')
    ]
]
, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Нажми кнопку')