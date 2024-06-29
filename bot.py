import os
from asyncio import run

from aiogram.filters import Command
from aiogram.types import BotCommand, Message
from dotenv import load_dotenv

from functions import start, info, stop, vacancy, helps, start_menu, register_name, register_phone, register_address, \
    register_position, register_finish, register_age, register_technology, register_require_time, register_salary
from states import SignUp

from aiogram import Bot, Dispatcher

load_dotenv()

TOKEN = os.getenv("bot_token")

dp = Dispatcher()


async def main(dp) -> None:
    bot = Bot(token=TOKEN)
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Bot ni ishga tushirish"),
            BotCommand(command="/info", description="Shaxsiy ma'lumotlarni olish"),
            BotCommand(command="/vacancy", description="Ishga e'lon berish"),
            BotCommand(command="/help", description="Yordam")
        ]
    )
    dp.startup.register(start)
    dp.message.register(vacancy, Command('vacancy'))
    dp.message.register(register_name, SignUp.name)
    dp.message.register(register_age, SignUp.age)
    dp.message.register(register_technology, SignUp.technology)
    dp.message.register(register_phone, SignUp.phone)
    dp.message.register(register_address, SignUp.address)
    dp.message.register(register_salary, SignUp.salary)
    dp.message.register(register_position, SignUp.position)
    dp.message.register(register_require_time, SignUp.require_time)
    dp.message.register(register_finish, SignUp.target)
    dp.message.register(info, Command('info'))
    dp.message.register(start_menu, Command('start'))
    dp.message.register(helps, Command('help'))
    dp.shutdown.register(stop)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    run(main(dp))