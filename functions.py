from pprint import pprint

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states import SignUp


async def info(message: Message, bot: Bot, state: FSMContext):
    profile = await bot.get_chat(chat_id=message.from_user.id)
    user = message.from_user
    user_photos = await message.from_user.get_profile_photos()

    data = f"{message.from_user.mention_html('USER')}" + ' INFO:\n\n'
    data += f"""Sizning ismingiz : {user.first_name} \nId raqamingiz: {user.id} \n"""
    if user.username:
        data += f"Siznig usernameiz @{user.username}\n"
    if user.last_name:
        data += f"Sizning familyangiz {user.last_name}\n"
    if profile.bio:
        data += f"Sizning bioingiz {profile.bio}\n"
    if user_photos.photos:
        await message.answer_photo(user_photos.photos[0][-1].file_id, caption=data, parse_mode="HTML")
    else:
        await message.answer(text=data, parse_mode="HTML")
    pprint(data)


async def helps(message: Message, bot: Bot, state: FSMContext):
    await message.answer("""
/start -> Botni ishga tushirish    
/help -> Commandlarni ko'rish    
/vacancy -> E'lon berish    
/stop --> Yuborilayotgan arizani bekor qilish
    """)


async def vacancy(message: Message, bot: Bot, state: FSMContext):
    await message.answer("""Ish joyi topish uchun ariza berish
Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""")

    await message.answer(
        "Ism, familiyangizni kiriting: "
    )
    await state.set_state(SignUp.name)


async def register_name(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("""🕑Yosh:\n\nYoshingini kiriting.\nMasalan,19""")
    await state.set_state(SignUp.age)


async def register_age(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("""📚 Texnologiya:\n\n
Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating.\nMasalan,\n\nPython, Java, C++, C#""")
    await state.set_state(SignUp.technology)


async def register_technology(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(technology=message.text)
    await message.answer("""📞 Aloqa:\n\n 
Bog`lanish uchun raqamingizni kiriting?\n
Masalan, +998 90 123 45 67""")
    await state.set_state(SignUp.phone)


async def register_phone(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("""🌐 Hudud:\n\n 
Qaysi hududdansiz?\n
Viloyat nomi, Toshkent shahar yoki\nRespublikani kiriting.""")
    await state.set_state(SignUp.address)


async def register_address(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(address=message.text)
    await message.answer("""💰 Narxi:\n\n
Tolov qilasizmi yoki Tekinmi?\n
Kerak bo`lsa, Summani kiriting:""")
    await state.set_state(SignUp.salary)


async def register_salary(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(salary=message.text)
    await message.answer("""👨🏻‍💻 Kasbi:\n\n
Ishlaysizmi yoki o`qiysizmi?\n
Masalan, Talaba""")
    await state.set_state(SignUp.position)


async def register_position(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(position=message.text)
    await message.answer("""🕰 Murojaat qilish vaqti:\n\n
Qaysi vaqtda murojaat qilish mumkin?\n
Masalan, 9:00 - 18:00""")
    await state.set_state(SignUp.require_time)


async def register_require_time(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(require_time=message.text)
    await message.answer("""🔎 Maqsad:\n\n
Maqsadingizni qisqacha yozib bering.""")
    await state.set_state(SignUp.target)


async def register_finish(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(target=message.text)
    data = await state.get_data()
    txt = f'''<b>Ish joyi kerak:</b>\n\n 
👨‍💼 Xodim: <b>{data.get("name")}</b>
🕑 Yosh:  {data.get("age")}
📚 Texnologiya: <b>{data.get("technology")}</b>
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {data.get("phone")}
🌐 Hudud: <b>{data.get("address")}</b>
💰 Narxi: {data.get("salary")}
👨🏻‍💻 Kasbi: {data.get("position")}
🕰 Murojaat qilish vaqti: {data.get("require_time")}
🔎 Maqsad: {data.get("target")}\n\n
{await hashtag(data)}
    '''
    await message.answer(text=txt, parse_mode="HTML")
    await message.answer("Tez Orada Kanalda Chop etiladi")
    await bot.send_message(chat_id="779534487", text=txt, parse_mode="HTML")
    await state.clear()


async def hashtag(data_):
    hashtags = f"#xodim "
    data_technology_str = data_.get("technology")
    for i in data_technology_str.split(','):
        hashtags += '#' + i.lower().strip() + ' '
    hashtags += '#' + data_.get("address")
    return hashtags


async def start_menu(message: Message, bot: Bot, state: FSMContext):
    await message.answer(f"Assalomu Alaykun {message.from_user.first_name} /help orqali menularni ko'ring")


async def start(bot: Bot):
    await bot.send_message(chat_id="779534487", text="Bot Ishga tushdi ✅")


async def stop(bot: Bot):
    await bot.send_message(chat_id="779534487", text="Bot To'xtadi ⚠️")


async def stop_command_answer(message: Message, bot: Bot, state: FSMContext):
    this_state = await state.get_state()
    if this_state is None:
        await message.answer('Siz xech qanday ariza yubormagansiz!')
    else:
        await message.answer('Arizangiz bekor qilindi!')
        await state.clear()