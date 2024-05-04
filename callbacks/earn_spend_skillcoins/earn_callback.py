from aiogram import F, types, Router

from keyboards.Inline.back_button import back_button_function

router = Router()


@router.callback_query(F.data == 'earn_skillcoins')
async def earn_skillcoins_button(callback: types.CallbackQuery):
    await callback.answer(text='Вы выбрали раздел заработать скиллкоины')

    # await callback.message.edit_text('Заработать скиллкоины')
    await callback.message.edit_caption(caption='Заработать скиллкоины')

    await callback.message.edit_reply_markup(reply_markup=back_button_function())
