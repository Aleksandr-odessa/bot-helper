from aiogram.fsm.state import StatesGroup, State


class Period(StatesGroup):
    choosing_day = State()
    choosing_office = State()
    get_mail = State()
    

class Month(StatesGroup):
    choosing_month = State()
