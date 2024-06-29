from aiogram.fsm.state import StatesGroup, State


class SignUp(StatesGroup):
    name = State()
    age = State()
    technology = State()
    phone = State()
    address = State()
    salary = State()
    position = State()
    require_time = State()
    target = State()