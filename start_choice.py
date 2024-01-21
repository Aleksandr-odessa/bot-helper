from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from dialogs import replicas
from keyboards.translate import button_periods


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(replicas["select_action"], reply_markup=button_periods())
    
    