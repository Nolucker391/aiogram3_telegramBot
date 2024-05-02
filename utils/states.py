from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    start = State()
    login = State()
    menu = State()