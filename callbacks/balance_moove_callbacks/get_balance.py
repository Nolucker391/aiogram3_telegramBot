from aiogram import F, types, Router

from keyboards.Inline.back_button import back_button_function

router = Router()


@router.callback_query(F.data == 'check_balance')
async def check_balance_button(callback: types.CallbackQuery):
    await callback.answer(text='Вы выбрали раздел просмотра баланса скиллкоинов')
    # await callback.message.answer(text='Выберите действие', reply_markup=builder_for_three_button.as_markup())
    await callback.message.edit_caption(caption='Ваш баланс')

    await callback.message.edit_reply_markup(reply_markup=back_button_function())