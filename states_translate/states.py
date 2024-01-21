from aiogram.fsm.state import StatesGroup, State


class Period(StatesGroup):
    choosing_period = State()
    choosing_office = State()
    

class Month(StatesGroup):
    choosing_month = State()
