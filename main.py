import asyncio
# from background import keep_alive
from fastapi import FastAPI
from config import Token
from aiogram import Bot, Dispatcher
from handlers import translation
import start_choice 


def setup_app():
    ap = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)

    async def main():
        bot = Bot(Token)
        dp = Dispatcher()
        dp.include_routers(start_choice.router, translation.router)
        await dp.start_polling(bot)

    @app.get("/")
    async def setup():
        asyncio.run(main())
        return "Webhook Updated"
    return ap


app = setup_app()
