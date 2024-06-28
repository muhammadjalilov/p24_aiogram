from pprint import pprint

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


async def get_info(message: Message, bot: Bot, state: FSMContext):
    profile = await bot.get_chat(chat_id=message.from_user.id)
    user = message.from_user
    user_photos = await message.from_user.get_profile_photos()

    data = user.mention_html("USER") + " INFO:\n\n"
    data += f"""Firstname: {user.first_name} \nId: {user.id} \n"""
    if user.username:
        data += f"Username @{user.username}\n"
    if user.last_name:
        data += f"Lastname: {user.last_name}\n"
    if profile.bio:
        data += f"Your bio: {profile.bio}\n"
    if user_photos.photos:
        await message.answer_photo(user_photos.photos[0][-1].file_id, caption=data, parse_mode="HTML")
    else:
        await message.answer(data, parse_mode="HTML")
    pprint(data)
