from aiogram import Router
from aiogram.types import Message


router = Router()


@router.edited_message()
async def on_edit(message: Message):
    await message.answer("Вы редактировали сообщение!")
