from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):

    authorization = State()
    change_account = State()
    get_contact = State()
    menu = State()