from aiogram.fsm.state import StatesGroup, State


class SignUp(StatesGroup):
    name = State()
    phone = State()
    address = State()
    position = State()
    salary = State()