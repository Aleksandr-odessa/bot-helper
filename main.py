import asyncio
# from background import keep_alive
from config import Token
from aiogram import Bot, Dispatcher
from handlers import translation
import start_choice 


async def main():
    bot = Bot(Token)
    dp = Dispatcher()
    dp.include_routers(start_choice.router, translation.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    # keep_alive()  # запускаем flask-сервер в отдельном потоке.
    asyncio.run(main())
