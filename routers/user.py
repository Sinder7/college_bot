import json
from datetime import datetime

from aiogram import Router, F
from aiogram.filters.command import CommandStart
from aiogram.types import Message, MessageEntity, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from utils.state_group import GroupName
from utils.days import get_name_weekday
from utils.get_data import get_day_data, get_week_data
from keyboards.reply import keyboards

router = Router()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    text="Добро пожаловать\nОтправляй название группы, чтобы получать расписание\nПример: Ис-32"
    entity_italic = MessageEntity(
        type='italic',
        offset=len('Добро пожаловать\nОтправляй название группы, чтобы получать расписание\nПример: '),
            length=4,
    )
    entities = [entity_italic]
    await message.answer(
            text=text,
            entities=entities,
        )
    await state.set_state(GroupName.user_group)

@router.message(GroupName.user_group)
async def get_group_name(message: Message, state: FSMContext):
    global user_data
    user_data = message.text.lower()
    await message.answer(
        text="Расписание на какое время нужно?",
        reply_markup=keyboards
    )
    await state.clear()


today = datetime.today().weekday()

@router.message(F.text == "Расписание на сегодня")
async def today_handler(message: Message, state: FSMContext):
    await message.answer(
        text=get_day_data(user_data, today+1),
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(GroupName.user_group)
    

@router.message(F.text == "Расписание на завтра")
async def tomorrow_handler(message: Message, state: FSMContext):
    await message.answer(
        text=get_day_data(user_data, today+2),
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(GroupName.user_group)



@router.message(F.text == "Расписание на неделю")
async def week_handler(message: Message, state: FSMContext):
    await message.answer(
        text=get_week_data(user_data),
        reply_markup=ReplyKeyboardRemove()
    )  
    await state.set_state(GroupName.user_group)

