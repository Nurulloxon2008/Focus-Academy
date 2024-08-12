from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.keyboard import Tugma, Chet_Tillar, Kursga_yozlish_tugmasi, Asosiy_Tugmalar, One_Button
from states.states import OrqagaState

keyboardHandlerRT: Router = Router()

class RegistrationStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_surname = State()
    waiting_for_phone = State()
    waiting_for_course = State()  

@keyboardHandlerRT.message(F.text == "Ta'lim Yo'nalishlari")
async def dasturlash_handler(message: Message, state : FSMContext):
    await state.set_state(OrqagaState.lvl5)  
    await message.answer("O'zizga tegshli bironta kursni tanlang", reply_markup=Asosiy_Tugmalar)

@keyboardHandlerRT.message(F.text == "IT Ta'lim")
async def dasturlash_handler(message: Message, state: FSMContext):
    await state.set_state(OrqagaState.lvl3)  
    await message.answer("Dasturlashning birorta qismini tanlang!", reply_markup=Tugma)

@keyboardHandlerRT.message(F.text == "Chet Tillari")
async def chet_tillari_handler(message: Message, state: FSMContext):
    await state.set_state(OrqagaState.lvl3) 
    await message.answer("Tilni tanlang:", reply_markup=Chet_Tillar)

@keyboardHandlerRT.message(F.text == "Matematika Kursi")
async def matematika_handler(message: Message, state: FSMContext):
    await state.set_state(OrqagaState.lvl3)  
    await message.answer("Matematika: \n\nMantiqiy matematika bo'yicha va oliy o'quv yurtlariga tayyorlanish uchun dars o'tiladi! \nTo'lov oyiga 300 000 so'm", reply_markup=Kursga_yozlish_tugmasi)

@keyboardHandlerRT.message(F.text == "Trading Kursi")
async def trading_handler(message: Message, state: FSMContext):
    await state.set_state(OrqagaState.lvl3)  
    await message.answer("Trading: \n\nKurs 3 oyga mo'ljallangan, 3ta moduldan iborat. \nHar bir modul yakunida imtixon mavjud. \nO'rgatiladigan texnologiyalar: \nClassic, SMC, ICT \nTo'lov oyiga 150$", reply_markup=Kursga_yozlish_tugmasi)

@keyboardHandlerRT.message(F.text == "Ingliz Tili")
async def ingliz_tili_handler(message: Message, state: FSMContext):
    await state.update_data(course="Ingliz Tili")
    await state.set_state(OrqagaState.lvl4)
    await message.answer("Ingliz tili: \n\nIelts va grammatika bo'yicha darslar bo'ladi! \nTo'lov oyiga 400 000 so'm.", reply_markup=Kursga_yozlish_tugmasi)

@keyboardHandlerRT.message(F.text == "Rus Tili")
async def rus_tili_handler(message: Message, state: FSMContext):
    await state.update_data(course="Rus Tili")
    await state.set_state(OrqagaState.lvl4)  
    await message.answer("Rus tili: \n\nCEFR sertifikati uchun tayyorlaymiz! \nTo'lov oyiga 350 000 so'm", reply_markup=Kursga_yozlish_tugmasi)

@keyboardHandlerRT.message(F.text == "Frontend")
async def frontend_handler(message: Message, state: FSMContext):
    await state.set_state(OrqagaState.lvl2)  
    await message.answer("Frontend: \n\nKurs 7 oyga mo'ljallangan, 4 moduldan iborat. \nHar bir modul yakunida imtixon mavjud. \nO'rgatiladigan texnologiyalar: \nHTML, CSS, Bootstrap, \nJavascript, Reactjs, Redux \nTo'lov oyiga 450 000 so'm.", reply_markup=Kursga_yozlish_tugmasi)

@keyboardHandlerRT.message(F.text == "Backend")
async def backend_handler(message: Message, state: FSMContext):
    await state.update_data(course="Backend")
    await state.set_state(OrqagaState.lvl2)  
    await message.answer("Ro'yxatdan o'ting!", reply_markup=Kursga_yozlish_tugmasi)

@keyboardHandlerRT.message(F.text == "Fullstack")
async def fullstack_handler(message: Message, state: FSMContext):
    await state.update_data(course="Fullstack")
    await state.set_state(OrqagaState.lvl2) 
    await message.answer("Ro'yxatdan o'ting!", reply_markup=Kursga_yozlish_tugmasi)




@keyboardHandlerRT.message(F.text == "🔙 Orqaga", OrqagaState.lvl1)
async def orqaga(message: Message, state: FSMContext):
    await state.set_state(OrqagaState.lvl5)
    await message.answer("🔙 Orqaga", reply_markup=Asosiy_Tugmalar)

@keyboardHandlerRT.message(F.text == "🔙 Orqaga", OrqagaState.lvl2)
async def orqaga2(message: Message, state: FSMContext):
    await state.set_state(OrqagaState.lvl1)
    await message.answer("🔙 Orqaga", reply_markup=Tugma)

@keyboardHandlerRT.message(F.text == "🔙 Orqaga", OrqagaState.lvl3)
async def orqaga3(message: Message, state : FSMContext):
    await state.set_state(OrqagaState.lvl5)
    await message.answer("🔙 Orqaga", reply_markup=Asosiy_Tugmalar)
    
@keyboardHandlerRT.message(F.text == "🔙 Orqaga", OrqagaState.lvl4)
async def orqaga4(message: Message, state: FSMContext):
    await state.set_state(OrqagaState.lvl1)
    await message.answer("🔙 Orqaga", reply_markup=Chet_Tillar)

@keyboardHandlerRT.message(F.text == "🔙 Orqaga")
async def orqaga5(message: Message):
    await message.answer("🔙 Orqaga", reply_markup=One_Button)  
    
@keyboardHandlerRT.message(F.text == "🔙 Orqaga", OrqagaState.lvl5)
async def Orqa6(message : Message):
    await message.answer("🔙 Orqaga", reply_markup=One_Button)
    
    
    


@keyboardHandlerRT.message(F.text == "Ro'yxatdan o'tish")
async def kursga_yozlish_handler(message: Message, state: FSMContext):
    await message.answer("Ismingizni kiriting:")
    await state.set_state(RegistrationStates.waiting_for_name)

@keyboardHandlerRT.message(RegistrationStates.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Familiyangizni kiriting:")
    await state.set_state(RegistrationStates.waiting_for_surname)

@keyboardHandlerRT.message(RegistrationStates.waiting_for_surname)
async def process_surname(message: Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await message.answer("Telefon raqamingizni kiriting:")
    await state.set_state(RegistrationStates.waiting_for_phone)

@keyboardHandlerRT.message(RegistrationStates.waiting_for_phone)
async def process_phone(message: Message, state: FSMContext):
    user_data = await state.get_data()
    name = user_data.get('name')
    surname = user_data.get('surname')
    phone = message.text
    course = user_data.get('course')  

    admin_id = 5589478752  
    await message.bot.send_message(admin_id, text=f"Yangi ro'yxatdan o'tish:\nIsm: {name}\nFamiliya: {surname}\nTelefon: {phone}\nKurs: {course}")

    await message.answer("Adminlar siz bilan aloqaga chiqishadi.")
    await state.clear()




