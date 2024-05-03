from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import Router

from aiogram.filters import Command

router = Router()

@router.message(Command('help'))
async def help_handler(message: Message) -> None:

    await message.answer("so <b>help</b>")
    await message.answer("so <s>help</s>")