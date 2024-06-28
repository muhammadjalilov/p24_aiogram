import os
from asyncio import run

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from functions import get_info

load_dotenv()

TOKEN = os.getenv("bot_token")

dp = Dispatcher()


async def start(bot: Bot):
    await bot.send_message(chat_id="779534487", text="Bot Ishga tushdi ✅")


async def stop(bot: Bot):
    await bot.send_message(chat_id="779534487", text="Bot To'xtadi ⚠️")


async def main(dp_) -> None:
    bot = Bot(token=TOKEN)
    dp_.startup.register(start)
    dp_.message.register(get_info)
    dp_.shutdown.register(stop)
    await dp_.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    run(main(dp))
