from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def contact_function():

    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Отправить контакт", request_contact=True))

    return builder