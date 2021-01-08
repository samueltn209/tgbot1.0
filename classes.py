from aiogram.dispatcher.filters.state import State, StatesGroup



class User():
    def __init__(self, new_user):
        self.user_id = new_user


class Form(StatesGroup):
    starting = State()
    first_step = State()
    second_step = State()
    admin_step = State()

