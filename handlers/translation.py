from aiogram import Router
from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from dialogs import replicas
from keyboards.translate import button_periods, button_office, button_months
from offices_translate import request_summ, check_data
from states_translate.states import Period, Month
from config import names, months
import logging

router = Router()
period_agency = []

file_log1 = logging.FileHandler("bot.log", "w")
console_out = logging.StreamHandler()
logging.basicConfig(handlers=(file_log1, console_out),
                    format='%(asctime)s, %(levelname)s, , %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.DEBUG)


@router.message(Month.choosing_month, F.text.in_(months))
async def month_choosen(message: Message, state: FSMContext):
    period_agency.append(message.text)
    try:
        summa: str = request_summ(period_agency)
        await message.answer(text=summa, reply_markup=button_periods())
        await state.clear()
        period_agency.clear()
    except ValueError:
        logging.info('error reqest summ month')


@router.message(Period.choosing_period)
async def period_chosen(message: Message, state: FSMContext):
    if check_data(str(message.text)):
        period_agency.append(message.text)
        await message.answer(text='Пожалуйста введите офис', reply_markup=button_office())
        await state.set_state(Period.choosing_office)
    else:
        await message.answer('Пожалуйста введите период')


@router.message(Period.choosing_office, F.text.in_(names))
async def office_chosen(message: Message, state: FSMContext):
    period_agency.append(message.text)
    print(period_agency)
    try:
        summa = request_summ(period_agency)
        await message.answer(text=summa, reply_markup=button_periods())
        await state.clear()
        period_agency.clear()
    except ValueError:
        logging.info('error reqest summ periods and office')


# Указать месяц или период и агенство
@router.message(F.text)
async def select_period(message: Message, state: FSMContext):
    if message.text == replicas["period"]:
        await message.answer(text=replicas["select_month"], reply_markup=button_months())
        await state.set_state(Month.choosing_month)
    elif message.text == replicas["period_agency"]:
        await message.answer(text='введите дату', reply_markup=button_periods())
        await state.set_state(Period.choosing_period)
    else:
        await message.answer(text='Сделайте выбор кнопками',
                             reply_markup=button_periods())