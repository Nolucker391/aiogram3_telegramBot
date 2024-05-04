from aiogram import F, types, Router

from keyboards.Inline.back_button import back_button_function

router = Router()


@router.callback_query(F.data == 'spend_skillcoins')
async def spend_skillcoins_button(callback: types.CallbackQuery):
    await callback.answer(text='Вы выбрали раздел списание скиллкоинов')

    await callback.message.edit_caption(caption='Списать скиллкоины')

    await callback.message.edit_reply_markup(reply_markup=back_button_function())