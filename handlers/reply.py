from aiogram import Router
from aiogram.types import Message


router = Router()


@router.edited_message()
async def start(message: Message):
    await message.answer("Вы редактировали сообщение!")
