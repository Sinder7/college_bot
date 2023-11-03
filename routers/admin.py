import os

from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters.command import Command

from filters.chat_type import ChatTypeFilter

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["group", "supergroup"])
)

@router.message(F.document)
async def download_json_file(message: Message,  bot: Bot):
    mime_type = message.document.mime_type
    if mime_type == 'application/json':
        os.remove("timetable/text.json")
        file_id = message.document.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        await bot.download_file(file_path, "timetable/text.json")
        await message.answer('Расписание обновлено')
    else:
        await message.answer('Файл должен быть JSON!')