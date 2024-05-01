#  polling
import asyncio
import os
from handlers.translation import router
from aiogram import Dispatcher, Bot
TOKEN = os.environ['TG_TOKEN']


async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_routers(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())



# web-chooks

# from handlers.translation import router
# import os
# from fastapi import FastAPI
# from aiogram import Dispatcher, Bot
# from aiogram import types
# app = FastAPI()

# os_inw = os.environ
# print(os_inw)
# TOKEN = os.environ['TG_TOKEN']
# TOKEN = "5899797856:AAFAs_vf7PJPql2uZJidQhfp31fcM1R6ISQ"
# WEBHOOK_HOST = "https://aleks.alwaysdata.net"
# WEBHOOK_PATH = f"/bot/{TOKEN}"
# WEBHOOK_URL = WEBHOOK_HOST+WEBHOOK_PATH
# dp = Dispatcher()
# bot = Bot(token=TOKEN)
# dp.include_routers(router)



# @app.post(WEBHOOK_PATH)
# async def bot_webhook(update: dict):
#     telegram_update = types.Update(**update)
#     await dp.feed_update(bot=bot, update=telegram_update)
#
#
# @app.get("/inst")
# async def setup():
#     await bot.set_webhook(url=WEBHOOK_URL, drop_pending_updates=True)
#     return "Webhook Updated"
#
#
# @app.get("/")
# async def instal():
#     return "test site"