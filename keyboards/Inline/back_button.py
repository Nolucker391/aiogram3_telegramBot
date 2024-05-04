from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def back_button_function():
    builder_for_first_button = InlineKeyboardBuilder()
    builder_for_first_button.add(
        types.InlineKeyboardButton(text='<< назад', callback_data='back'),
    )

    return builder_for_first_button.as_markup()
