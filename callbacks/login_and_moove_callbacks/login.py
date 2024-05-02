from aiogram import F, types, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from utils.states import Form

router = Router()

@router.callback_query(Form.start, F.data == 'Login')
async def send_back_button(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()

    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Отправить контакт", request_contact=True))

    # builder_inline = InlineKeyboardBuilder()
    # builder_inline.add(types.InlineKeyboardButton(text='<< вернуться назад', callback_data='back_back'))

    await callback.message.answer(
        'Введите номер телефона или поделитесь контактом, появившемся внизу кнопкой "Отправить контакт" ',
        reply_markup=builder.as_markup(resize_keyboard=True),
    )

    await state.set_state(Form.login)


@router.message(Form.login)
async def phone_number_function(message: Message, state: FSMContext):

    text_for_user = ('Вы успешно вошли в систему!\n'
                     'Вот твой основной функионал: \n')
    try:

        if message.contact.phone_number:
            await message.answer(text=text_for_user, reply_markup=types.ReplyKeyboardRemove())
            await state.set_state(Form.menu)
    except AttributeError:
        await message.answer('Отправьте ваш номер телефона')