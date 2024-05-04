from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

def student_menu():
    builder_inline = InlineKeyboardBuilder()

    builder_inline.row(
        types.InlineKeyboardButton(text='заработать скиллкоины', callback_data='earn_skillcoins'),
        types.InlineKeyboardButton(text='списать скиллкоины', callback_data='spend_skillcoins')
    )
    builder_inline.row(
        types.InlineKeyboardButton(text='посмотреть баланс', callback_data='check_balance'),
        types.InlineKeyboardButton(text='перенести аккаунт', callback_data='moove_account')
    )
    builder_inline.row(
        types.InlineKeyboardButton(text='выйти из аккаунта', callback_data='quit_account_on_system')
    )

    return builder_inline