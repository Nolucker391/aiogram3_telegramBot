from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import Router, Bot

from aiogram.filters import Command
from keyboards.Inline.main_menu_keyboard.menu_of_student import student_menu
from role_decorator.main import role_decorator
from role_decorator.users import User
from utils.states import Form

router = Router()


@router.message(Command('menu'))
@role_decorator([User.student, User.admin])
async def main_menu(message: Message, state: FSMContext) -> None:

    builder_inline_of_student = student_menu()
    constructor = '_' * 31
    photo_path = 'images/logo_main_menu/skb-logo.png'

    await message.answer_photo(
            photo=types.FSInputFile(path=photo_path),
            caption=f'Главное меню\n'
                    f'{constructor}\n'
                    f'ФИО: \n'
                    f'направление: \n',
            reply_markup=builder_inline_of_student.as_markup()
    )

    await state.set_state(Form.menu)

    # await message.answer(
    #     text=
    #     f'Главное меню\n'
    #     f'{constructor}\n'
    #     f'ФИО: \n'
    #     f'направление: \n',
    #     reply_markup=builder_inline_of_student.as_markup()
    # )

    #builder_inline_of_admin = admin_menu(message)
    #builder_inline_of_curator = curator_menu(message)

    # await message.answer(
    #     text=f'Главное меню\n'
    #          f'{constructor}\n'
    #          f'Информация: \n',
    #     reply_markup=builder_inline_of_curator.as_markup()
    # )
    #
    # await message.answer(
    #     text=f'Главное меню\n'
    #         f'{constructor}\n'
    #         f'Информация: \n',
    #     reply_markup=builder_inline_of_admin.as_markup()
    # )


@router.message(Form.menu)
async def menu(message: Message, state: FSMContext):
    if message.text:
        await message.delete()
        show_alert = True
        print("show_alert =", show_alert)
        await message.answer(text='Выберите действие из списка!', show_alert=True)

