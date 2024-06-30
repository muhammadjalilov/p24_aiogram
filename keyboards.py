from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

contact_location_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Share contact", request_contact=True),
            KeyboardButton(text="Share location", request_location=True)
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Tugmalardan birini tanlang:',
    is_persistent=True
)

channel_list = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="null", url="https://t.me/djalilovv_mukhammad"),
        ],
        [
            InlineKeyboardButton(text="Tekshirish ✅", callback_data="check_subscription")
        ]
    ]
)
