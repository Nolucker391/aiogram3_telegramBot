from aiogram import F, types, Router

from keyboards.Inline.back_button import back_button_function

router = Router()


@router.callback_query(F.data == 'moove_account')
async def moove_account_button(callback: types.CallbackQuery):
    await callback.answer(
        text=
        'Предупреждение! \n'
        'Перенос аккаунта может привести к потере данных\n'
        'Следуйте инструкции.',
        show_alert=True
    )
    await callback.message.edit_caption(caption='Раздел переноса аккаунта')

    await callback.message.edit_reply_markup(reply_markup=back_button_function())