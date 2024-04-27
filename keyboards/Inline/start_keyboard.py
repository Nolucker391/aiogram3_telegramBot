from aiogram import types

from aiogram.utils.keyboard import InlineKeyboardBuilder

def start_keyboard():

    builder = InlineKeyboardBuilder()

    builder.row(
            types.InlineKeyboardButton(text='➥ Авторизоваться', callback_data='Login')
    )
    builder.row(types.InlineKeyboardButton(text='➥ Сменить аккаунт', callback_data='change_accout'))

    return builder.as_markup()