from aiogram import F, types, Router

from keyboards.Inline.main_menu_keyboard.menu_of_student import student_menu

router = Router()


@router.callback_query(F.data == 'back')
async def send_back_button(callback: types.CallbackQuery):
    builder_main_menu = student_menu()
    constructor = '_' * 31

    text = (
        f'Главное меню\n'
        f'{constructor}\n'
        f'ФИО: \n'
        f'направление: \n'
    )

    await callback.message.edit_caption(caption=text)

    await callback.message.edit_reply_markup(reply_markup=builder_main_menu.as_markup())
