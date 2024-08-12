from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.keyboard import One_Button

startRT: Router = Router()

@startRT.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        f"Assalomu alaykum, {message.from_user.first_name}. Focus Academyga qiziqish \nbildirganingizdan minnatdormiz. \nQaysi kursimiz siz uchun qiziq bo'ldi.",
        reply_markup=One_Button
    )
 