from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from dialogs import replicas
from config import names, months, days
from offices_translate2 import GetCountForMonth

def button_main() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text=replicas["month"])
    keyboard.button(text=replicas["period_agency"])
    keyboard.adjust(2)
    return keyboard.as_markup(resize_keyboard=True)


def button_office() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    for office in names:
        keyboard.add(types.KeyboardButton(text=office))
    keyboard.adjust(5)
    return keyboard.as_markup(resize_keyboard=True)


def button_months() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    for month in months:
        keyboard.add(types.KeyboardButton(text=month))
    keyboard.adjust(6)
    return keyboard.as_markup(resize_keyboard=True)


def button_days() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    for day in days:
        keyboard.add(types.KeyboardButton(text=day))
    keyboard.adjust(8)
    return keyboard.as_markup(resize_keyboard=True)

