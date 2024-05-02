from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext

from keyboards.Inline.start_keyboard import start_keyboard
from utils.states import Form

router = Router()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    constructor = '_' * 33
    content_text = (f'Приветствую, дорогой пользователь - <b>{message.from_user.full_name}</b>\n'
                    f'\nДанный телеграмм-бот предназначен...[соответствуйющий текст]\n'
                    f'{constructor}\n'
                    f'Пройдите форму авторизации, для дальнейших коммуникаций')

    await message.answer(text=content_text, reply_markup=start_keyboard())

    await state.set_state(Form.start)
