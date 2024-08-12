from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

One_Button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ta'lim Yo'nalishlari")]
    ],
    resize_keyboard=True
)

Asosiy_Tugmalar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="IT Ta'lim"), KeyboardButton(text="Trading Kursi")],
        [KeyboardButton(text="Matematika Kursi"), KeyboardButton(text="Chet Tillari")],
        [KeyboardButton(text="🔙 Orqaga")]
    ],
    resize_keyboard=True
)


Chet_Tillar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ingliz Tili"), KeyboardButton(text="Rus Tili")],
        [KeyboardButton(text="🔙 Orqaga")]
    ],
    resize_keyboard=True
)


Tugma = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Frontend"), KeyboardButton(text="Backend")],
        [KeyboardButton(text="Fullstack"), KeyboardButton(text="🔙 Orqaga")]
    ],
    resize_keyboard=True
)


Kursga_yozlish_tugmasi = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ro'yxatdan o'tish")],
        [KeyboardButton(text="🔙 Orqaga")]
    ],
    resize_keyboard=True
)
