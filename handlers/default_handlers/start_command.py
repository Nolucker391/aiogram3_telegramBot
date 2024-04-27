from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram import Router
from keyboards.Inline.start_keyboard import start_keyboard

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    constructor = '_' * 33
    content_text = (f'Приветствую, дорогой пользователь - {router.html.bold(message.from_user.full_name)}\n'
                    f'\nДанный телеграмм-бот предназначен...[соответствуйющий текст]\n'
                    f'{constructor}\n'
                    f'Пройдите форму авторизации, для дальнейших коммуникаций')

    await message.answer(text=content_text, reply_markup=start_keyboard())
