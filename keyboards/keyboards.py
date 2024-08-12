from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

Asosiy_Tugmalar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Dasturlash"), KeyboardButton(text="Trading")],
        [KeyboardButton(text="Matematika"),KeyboardButton(text="Chet tillari")]
        [KeyboardButton(text="🔙 Orqaga")]
    ],
    resize_keyboard=True
)
