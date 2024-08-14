from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from states.state import ArizaOlish
from keyboards.keyboards import finish
from keyboards.keyboards import ustoz_shogird
from loader import bot

startRT : Router = Router()

malumotlar = {}

@startRT.message(CommandStart())
async def start(msg: Message , state: FSMContext):
    await state.clear()
    await msg.answer(f"Assalom alaykum {msg.from_user.username} kanalining rasmiy botiga xush kelibsiz!", reply_markup=ustoz_shogird)

@startRT.message(F.text == "Sherik kerak")
async def start(msg: Message, state:FSMContext):
    await state.set_state(ArizaOlish.FISH)
    await msg.answer("Sherik topish uchun ariza berish: \n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering. \nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await msg.answer("Ism va Familiyangizni kiriting?") 

@startRT.message(F.text == "Ish joyi kerak")
async def start(msg: Message, state:FSMContext):
    await state.clear()
    await state.set_state(ArizaOlish.FISH)
    await msg.answer("Ish joyi topish uchun ariza berish: \n\nHozir sizga birnecha savollar beriladi.  \nHar biriga javob bering.  \nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await msg.answer("Ism va Familiyangizni kiriting?")

@startRT.message(F.text == "Hodim kerak")
async def start(msg: Message, state: FSMContext):
    await state.clear()
    await state.set_state(ArizaOlish.Idora)
    await msg.answer(f"Xodim topish uchun ariza berish \n\nHozir sizga birnecha savollar beriladi: \nHar biriga javob bering. \nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await msg.answer("🎓 Idora nomi?") 

@startRT.message(F.text == "Ustoz kerak")
async def start(msg: Message, state: FSMContext):
    await state.clear()
    await state.set_state(ArizaOlish.FISH)
    await msg.answer(f"Ustoz topish uchun ariza berish: \n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering. \nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await msg.answer("Ism va Familiyangizni kiriting?")

@startRT.message(F.text == "Shogird kerak")
async def start(msg: Message, state: FSMContext):
    await state.clear()
    await state.set_state(ArizaOlish.FISH)
    await msg.answer(f"Shogird topish uchun ariza berish: \n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering. \nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await msg.answer("Ism va Familiyangizni kiriting")

@startRT.message(ArizaOlish.FISH)
async def start(msg: Message, state:FSMContext):
    malumotlar["FISH"] = msg.text
    await state.set_state(ArizaOlish.Yosh)
    await msg.answer("Yosh: \n\nYoshingizni kiriting? \nMasalan; 20.")

@startRT.message(ArizaOlish.Yosh)
async def start(msg: Message, state:FSMContext):
    malumotlar["Yosh"] = msg.text
    await state.set_state(ArizaOlish.Texno)
    await msg.answer("Texnologiya: \n\nTalab qilinadigan texnologiyani kiriting? \nMasalan; Python.")

@startRT.message(ArizaOlish.Texno)
async def start(msg: Message, state:FSMContext):
    malumotlar["Texno"] = msg.text
    await state.set_state(ArizaOlish.Nomer)
    await msg.answer("Aloqa: \n\nBog'lanish uchun raqamingizni kiriting? \nMasalan; +998 davom ettiring...")

@startRT.message(ArizaOlish.Nomer)
async def start(msg: Message, state:FSMContext):
    malumotlar["Nomer"] = msg.text
    await state.set_state(ArizaOlish.Manzil)
    await msg.answer("Manzil: \n\nQaysi hududdansiz? \nViloyat nomi, Toshkent shahar yoki \nRespublikani kiriting.")

@startRT.message(ArizaOlish.Manzil)
async def start(msg: Message, state:FSMContext):
    malumotlar["Manzil"] = msg.text
    await state.set_state(ArizaOlish.Narxi)
    await msg.answer("Narxi: \n\nTo'lov qilasizmi yoki Tekinmi? \nKerak bo'lsa, Summani kiriting?")

@startRT.message(ArizaOlish.Narxi)
async def start(msg: Message, state:FSMContext):
    malumotlar["Narxi"] = msg.text
    await state.set_state(ArizaOlish.Kasb)
    await msg.answer("Ishlaysizmi yoki o'qiysizmi? \nMasalan; Talaba")

@startRT.message(ArizaOlish.Kasb)
async def start(msg: Message, state:FSMContext):
    malumotlar["Kasb"] = msg.text
    await state.set_state(ArizaOlish.Murojatvaqt)
    await msg.answer("Murojaat qilish vaqti: \n\nQaysi vaqtda murojaat qilish mumkin? \nMasalan; 9:00-20:00")

@startRT.message(ArizaOlish.Murojatvaqt)
async def start(msg: Message, state:FSMContext):
    malumotlar["Murojatvaqt"] = msg.text
    await state.set_state(ArizaOlish.Maqsad)
    await msg.answer("Maqsad: \n\nMaqsadingiz haqida qisqacha yozib qoldiring")


@startRT.message(F.text == "Ha")
async def ha(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("Admin ko'rib chiqadi")
    await bot.send_message(chat_id=6010716128 , text=f"""
    
Sherik kerak:

🏅 Sherik: {malumotlar['FISH']}
🕑 Yosh: {malumotlar['Yosh']}
📚 Texnologiya: {malumotlar['Texno']}
🇺🇿 Telegram: {msg.from_user.username}
📞 Aloqa: {malumotlar['Nomer']}
🌐 Hudud: {malumotlar['Manzil']}
💰 Narxi: {malumotlar['Narxi']}
👨🏻‍💻 Kasbi:{malumotlar['Kasb']}
🕰 Murojaat qilish vaqti:{malumotlar['Murojatvaqt']}
🔎 Maqsad: malumotlar{malumotlar['Maqsad']}

""", reply_markup=ustoz_shogird)

@startRT.message(F.text == "Yo'q")
async def yoq(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("bekor qilindi")

@startRT.message(ArizaOlish.Maqsad)
async def start(msg: Message):
    malumotlar["Maqsad"] = msg.text
    await msg.answer(f"""
Sherik kerak:

🏅 Sherik: {malumotlar['FISH']}
🕑 Yosh: {malumotlar['Yosh']}
📚 Texnologiya: {malumotlar['Texno']}
🇺🇿 Telegram: {msg.from_user.username}
📞 Aloqa: {malumotlar['Nomer']}
🌐 Hudud: {malumotlar['Manzil']}
💰 Narxi: {malumotlar['Narxi']}
👨🏻‍💻 Kasbi:{malumotlar['Kasb']}
🕰 Murojaat qilish vaqti:{malumotlar['Murojatvaqt']}
🔎 Maqsad: malumotlar{malumotlar['Maqsad']}
""")
    await msg.answer("Barcha ma'lumotlar to'g'rimi", reply_markup=finish)

 

@startRT.message(ArizaOlish.FISH)
async def start(msg: Message, state:FSMContext):
    malumotlar["FISH"] = msg.text
    await state.set_state(ArizaOlish.Yosh)
    await msg.answer("Yosh: \n\nYoshingizni kiriting? \nMasalan; 20.")

@startRT.message(ArizaOlish.Yosh)
async def start(msg: Message, state:FSMContext):
    malumotlar["Yosh"] = msg.text
    await state.set_state(ArizaOlish.Texno)
    await msg.answer("Texnologiya: \n\nTalab qilinadigan texnologiyani kiriting? \nMasalan; Python.")

@startRT.message(ArizaOlish.Texno)
async def start(msg: Message, state:FSMContext):
    malumotlar["Texno"] = msg.text
    await state.set_state(ArizaOlish.Nomer)
    await msg.answer("Aloqa: \n\nBog'lanish uchun raqamingizni kiriting? \nMasalan; +998 davom ettiring...")

@startRT.message(ArizaOlish.Nomer)
async def start(msg: Message, state:FSMContext):
    malumotlar["Nomer"] = msg.text
    await state.set_state(ArizaOlish.Manzil)
    await msg.answer("Manzil: \n\nQaysi hududdansiz? \nViloyat nomi, Toshkent shahar yoki \nRespublikani kiriting.")

@startRT.message(ArizaOlish.Manzil)
async def start(msg: Message, state:FSMContext):
    malumotlar["Manzil"] = msg.text
    await state.set_state(ArizaOlish.Narxi)
    await msg.answer("Narxi: \n\nTo'lov qilasizmi yoki Tekinmi? \nKerak bo'lsa, Summani kiriting?")

@startRT.message(ArizaOlish.Narxi)
async def start(msg: Message, state:FSMContext):
    malumotlar["Narxi"] = msg.text
    await state.set_state(ArizaOlish.Kasb)
    await msg.answer("Ishlaysizmi yoki o'qiysizmi? \nMasalan; Talaba")

@startRT.message(ArizaOlish.Kasb)
async def start(msg: Message, state:FSMContext):
    malumotlar["Kasb"] = msg.text
    await state.set_state(ArizaOlish.Murojatvaqt)
    await msg.answer("Murojaat qilish vaqti: \n\nQaysi vaqtda murojaat qilish mumkin? \nMasalan; 9:00-20:00")

@startRT.message(ArizaOlish.Murojatvaqt)
async def start(msg: Message, state:FSMContext):
    malumotlar["Murojatvaqt"] = msg.text
    await state.set_state(ArizaOlish.Maqsad)
    await msg.answer("Maqsad: \n\nMaqsadingiz haqida qisqacha yozib qoldiring")

@startRT.message(F.text == "Ha")
async def ha(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("Admin ko'rib chiqadi")
    await bot.send_message(chat_id=6010716128 , text=f"""
    
Ish joyi kerak:

👨‍💼 Xodim: {malumotlar['FISH']}
🕑 Yosh: {malumotlar['Yosh']}
📚 Texnologiya: {malumotlar['Texno']}
🇺🇿 Telegram: {msg.from_user.username}
📞 Aloqa: {malumotlar['Nomer']}
🌐 Hudud: {malumotlar['Manzil']}
💰 Narxi: {malumotlar['Narxi']}
👨🏻‍💻 Kasbi: { malumotlar['Kasb']}
🕰 Murojaat vaqti: {malumotlar['Murojatvaqt']}
🔎 Maqsad: {malumotlar['Maqsad']}
""", reply_markup=ustoz_shogird)
    
@startRT.message(F.text == "Yo'q")
async def yoq(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("bekor qilindi")

@startRT.message(ArizaOlish.Maqsad)
async def start(msg: Message):
    malumotlar["Maqsad"] = msg.text
    await msg.answer(f"""
    Ish joyi kerak:

👨‍💼 Xodim: {malumotlar['FISH']}
🕑 Yosh: {malumotlar['Yosh']}
📚 Texnologiya: {malumotlar['Texno']}
🇺🇿 Telegram: {msg.from_user.username}
📞 Aloqa: {malumotlar['Nomer']}
🌐 Hudud: {malumotlar['Manzil']}
💰 Narxi: {malumotlar['Narxi']}
👨🏻‍💻 Kasbi: { malumotlar['Kasb']}
🕰 Murojaat vaqti: {malumotlar['Murojatvaqt']}
🔎 Maqsad: {malumotlar['Maqsad']}

""")
    await msg.answer("Barcha ma'lumotlar to'g'rimi", reply_markup=finish)

@startRT.message(ArizaOlish.Idora)
async def start(msg: Message, state:FSMContext):
    malumotlar["Idora"] = msg.text
    await state.set_state(ArizaOlish.Texno)
    await msg.answer("Texnologiya: \n\nTalab qilinadigan texnologiyalarni kiriting? \nTexnologiya nomlarini vergul bilan ajrating. Masalan, \n\nJava, C++, C#")

@startRT.message(ArizaOlish.Texno)
async def start(msg: Message, state:FSMContext):
    malumotlar["Texno"] = msg.text
    await state.set_state(ArizaOlish.Nomer)
    await msg.answer("Aloqa: \n\nBog`lanish uchun raqamingizni kiriting? \nMasalan, +998 davom ettiring...")

@startRT.message(ArizaOlish.Nomer)
async def start(msg: Message, state:FSMContext):
    malumotlar["Nomer"] = msg.text
    await state.set_state(ArizaOlish.Manzil)
    await msg.answer("Manzil \n\nQaysi hududdansiz? \nViloyat nomi, Toshkent shahar yoki Respublikani kiriting")

@startRT.message(ArizaOlish.Manzil)
async def start(msg: Message, state:FSMContext):
    malumotlar["Manzil"] = msg.text
    await state.set_state(ArizaOlish.Masulismsharifi)
    await msg.answer("Mas'ul ism sharifi?")

@startRT.message(ArizaOlish.Masulismsharifi)
async def start(msg: Message, state:FSMContext):
    malumotlar["Masulismsharifi"] = msg.text
    await state.set_state(ArizaOlish.Murojatvaqt)
    await msg.answer("Qaysi vaqtda murojaat qilish mumkin? \nMasalan, 9:00 - 18:00")

@startRT.message(ArizaOlish.Murojatvaqt)
async def start(msg: Message, state:FSMContext):
    malumotlar["Murojatvaqt"] = msg.text
    await state.set_state(ArizaOlish.Ishvaqt)
    await msg.answer("Ish vaqtini kiriting?")

@startRT.message(ArizaOlish.Ishvaqt)
async def start(msg: Message, state:FSMContext):
    malumotlar["Ishvaqt"] = msg.text
    await state.set_state(ArizaOlish.Maosh)
    await msg.answer("Maoshni kiriting?")

@startRT.message(ArizaOlish.Maosh)
async def start(msg: Message, state:FSMContext):
    malumotlar["Maosh"] = msg.text
    await state.set_state(ArizaOlish.Qoshimcha)
    await msg.answer("Qo`shimcha ma`lumotlar?")

@startRT.message(F.text == "Ha")
async def ha(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("Admin ko'rib chiqadi")
    await bot.send_message(chat_id=6010716128 , text=f"""

Xodim kerak:

                           🏢 Idora: {malumotlar['Idora']}
📚 Texnologiya:  {malumotlar['Texno']}
🇺🇿 Telegram:  {msg.from_user.username}
📞 Aloqa: {malumotlar['Aloqa']}
🌐 Hudud:  {malumotlar['Hudud']}
✍️ Mas'ul: {malumotlar['Masulismsharifi']}
🕰 Murojaat vaqti: {malumotlar['Murojatvaqt']}
🕰 Ish vaqti: {malumotlar['Ishvaqt']}
💰 Maosh: {malumotlar['Maosh']}
‼️ Qo`shimcha: {malumotlar['Qoshimcha']}
                                            
""" , reply_markup=ustoz_shogird)
    
@startRT.message(F.text == "Yo'q")
async def yoq(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("bekor qilindi")

@startRT.message(ArizaOlish.Qoshimcha)
async def start(msg: Message):
    malumotlar["Qoshimcha"] = msg.text
    await msg.answer(f"""
Xodim kerak:

🏢 Idora: {malumotlar['Idora']}
📚 Texnologiya:  {malumotlar['Texno']}
🇺🇿 Telegram:  {msg.from_user.username}
📞 Aloqa: {malumotlar['Aloqa']}
🌐 Hudud:  {malumotlar['Hudud']}
✍️ Mas'ul: {malumotlar['Masulismsharifi']}
🕰 Murojaat vaqti: {malumotlar['Murojatvaqt']}
🕰 Ish vaqti: {malumotlar['Ishvaqt']}
💰 Maosh: {malumotlar['Maosh']}
‼️ Qo`shimcha: {malumotlar['Qoshimcha']}
""")
    await msg.answer("Barcha ma'lumotlar to'g'rimi", reply_markup=finish)

@startRT.message(ArizaOlish.FISH)
async def start(msg: Message, state:FSMContext):
    malumotlar["FISH"] = msg.text
    await state.set_state(ArizaOlish.Yosh)
    await msg.answer("Yosh: \n\nYoshingizni kiriting? \nMasalan; 20.")

@startRT.message(ArizaOlish.Yosh)
async def start(msg: Message, state:FSMContext):
    malumotlar["Yosh"] = msg.text
    await state.set_state(ArizaOlish.Texno)
    await msg.answer("Texnologiya: \n\nTalab qilinadigan texnologiyani kiriting? \nMasalan; Python.")

@startRT.message(ArizaOlish.Texno)
async def start(msg: Message, state:FSMContext):
    malumotlar["Texno"] = msg.text
    await state.set_state(ArizaOlish.Nomer)
    await msg.answer("Aloqa: \n\nBog'lanish uchun raqamingizni kiriting? \nMasalan; +998 davom ettiring...")

@startRT.message(ArizaOlish.Nomer)
async def start(msg: Message, state:FSMContext):
    malumotlar["Nomer"] = msg.text
    await state.set_state(ArizaOlish.Manzil)
    await msg.answer("Manzil: \n\nQaysi hududdansiz? \nViloyat nomi, Toshkent shahar yoki \nRespublikani kiriting.")

@startRT.message(ArizaOlish.Manzil)
async def start(msg: Message, state:FSMContext):
    malumotlar["Manzil"] = msg.text
    await state.set_state(ArizaOlish.Narxi)
    await msg.answer("Narxi: \n\nTo'lov qilasizmi yoki Tekinmi? \nKerak bo'lsa, Summani kiriting?")

@startRT.message(ArizaOlish.Narxi)
async def start(msg: Message, state:FSMContext):
    malumotlar["Narxi"] = msg.text
    await state.set_state(ArizaOlish.Kasb)
    await msg.answer("Ishlaysizmi yoki o'qiysizmi? \nMasalan; Talaba")

@startRT.message(ArizaOlish.Kasb)
async def start(msg: Message, state:FSMContext):
    malumotlar["Kasb"] = msg.text
    await state.set_state(ArizaOlish.Murojatvaqt)
    await msg.answer("Murojaat qilish vaqti: \n\nQaysi vaqtda murojaat qilish mumkin? \nMasalan; 9:00-20:00")

@startRT.message(ArizaOlish.Murojatvaqt)
async def start(msg: Message, state:FSMContext):
    malumotlar["Murojatvaqt"] = msg.text
    await state.set_state(ArizaOlish.Maqsad)
    await msg.answer("Maqsad: \n\nMaqsadingiz haqida qisqacha yozib qoldiring")

@startRT.message(F.text == "Ha")
async def ha(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("Admin ko'rib chiqadi")
    await bot.send_message(chat_id=6010716128 , text=f"""        
Ustoz kerak:

🎓 Shogird: {malumotlar['FISH']}
🌐 Yosh: {malumotlar['Yosh']}
📚 Texnologiya:  {malumotlar['Texno']}
🇺🇿 Telegram:  {msg.from_user.username}
📞 Aloqa: {malumotlar['Nomer']}
🌐 Hudud:  {malumotlar['Manzil']}
💰 Narxi:  {malumotlar['Narxi']}
👨🏻‍💻 Kasbi:  {malumotlar['Kasb']}
🕰 Murojaat qilish vaqti:{malumotlar['Murojatvaqt']}
🔎 Maqsad:{malumotlar['Maqsad']}
                           
""" , reply_markup=ustoz_shogird)
    
@startRT.message(F.text == "Yo'q")
async def yoq(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("bekor qilindi")

@startRT.message(ArizaOlish.Maqsad)
async def start(msg: Message):
    malumotlar["Maqsad"] = msg.text
    await msg.answer(f"""
    Ustoz kerak:

🎓 Shogird: {malumotlar['FISH']}
🌐 Yosh: {malumotlar['Yosh']}
📚 Texnologiya:  {malumotlar['Texno']}
🇺🇿 Telegram:  {msg.from_user.username}
📞 Aloqa: {malumotlar['Nomer']}
🌐 Hudud:  {malumotlar['Manzil']}
💰 Narxi:  {malumotlar['Narxi']}
👨🏻‍💻 Kasbi:  {malumotlar['Kasb']}
🕰 Murojaat qilish vaqti:{malumotlar['Murojatvaqt']}
🔎 Maqsad:{malumotlar['Maqsad']}
""")
    await msg.answer("Barcha ma'lumotlar to'g'rimi", reply_markup=finish)

@startRT.message(ArizaOlish.FISH)
async def start(msg: Message, state:FSMContext):
    malumotlar["FISH"] = msg.text
    await state.set_state(ArizaOlish.Yosh)
    await msg.answer("Yosh: \n\nYoshingizni kiriting? \nMasalan; 20.")

@startRT.message(ArizaOlish.Yosh)
async def start(msg: Message, state:FSMContext):
    malumotlar["Yosh"] = msg.text
    await state.set_state(ArizaOlish.Texno)
    await msg.answer("Texnologiya: \n\nTalab qilinadigan texnologiyani kiriting? \nMasalan; Python.")

@startRT.message(ArizaOlish.Texno)
async def start(msg: Message, state:FSMContext):
    malumotlar["Texno"] = msg.text
    await state.set_state(ArizaOlish.Nomer)
    await msg.answer("Aloqa: \n\nBog'lanish uchun raqamingizni kiriting? \nMasalan; +998 davom ettiring...")

@startRT.message(ArizaOlish.Nomer)
async def start(msg: Message, state:FSMContext):
    malumotlar["Nomer"] = msg.text
    await state.set_state(ArizaOlish.Manzil)
    await msg.answer("Manzil: \n\nQaysi hududdansiz? \nViloyat nomi, Toshkent shahar yoki \nRespublikani kiriting.")

@startRT.message(ArizaOlish.Manzil)
async def start(msg: Message, state:FSMContext):
    malumotlar["Manzil"] = msg.text
    await state.set_state(ArizaOlish.Narxi)
    await msg.answer("Narxi: \n\nTo'lov qilasizmi yoki Tekinmi? \nKerak bo'lsa, Summani kiriting?")

@startRT.message(ArizaOlish.Narxi)
async def start(msg: Message, state:FSMContext):
    malumotlar["Narxi"] = msg.text
    await state.set_state(ArizaOlish.Kasb)
    await msg.answer("Ishlaysizmi yoki o'qiysizmi? \nMasalan; Talaba")

@startRT.message(ArizaOlish.Kasb)
async def start(msg: Message, state:FSMContext):
    malumotlar["Kasb"] = msg.text
    await state.set_state(ArizaOlish.Murojatvaqt)
    await msg.answer("Murojaat qilish vaqti: \n\nQaysi vaqtda murojaat qilish mumkin? \nMasalan; 9:00-20:00")

@startRT.message(ArizaOlish.Murojatvaqt)
async def start(msg: Message, state:FSMContext):
    malumotlar["Murojatvaqt"] = msg.text
    await state.set_state(ArizaOlish.Maqsad)
    await msg.answer("Maqsad: \n\nMaqsadingiz haqida qisqacha yozib qoldiring")

@startRT.message(F.text == "Ha")
async def ha(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("Admin ko'rib chiqadi")
    await bot.send_message(chat_id=6010716128 , text=f"""    
Shogird kerak:

🎓 Ustoz: {malumotlar['FISH']}
🌐 Yosh: {malumotlar['Yosh']}
📚 Texnologiya: {malumotlar['Texno']}
🇺🇿 Telegram: {msg.from_user.username}
📞 Aloqa:{malumotlar['Nomer']}
🌐 Hudud: {malumotlar['Manzil']}
💰 Narxi: {malumotlar['Narxi']}
👨🏻‍💻 Kasbi: {malumotlar['Kasb']}
🕰 Murojaat qilish vaqti: {malumotlar['Murojatvaqt']}
🔎 Maqsad:{malumotlar['Maqsad']}""" , reply_markup=ustoz_shogird)
    
@startRT.message(F.text == "Yo'q")
async def yoq(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("bekor qilindi")

@startRT.message(ArizaOlish.Maqsad)
async def start(msg: Message):
    malumotlar["Maqsad"] = msg.text
    await msg.answer(f"""
    Shogird kerak:

🎓 Ustoz: {malumotlar['FISH']}
🌐 Yosh: {malumotlar['Yosh']}
📚 Texnologiya: {malumotlar['Texno']}
🇺🇿 Telegram: {msg.from_user.username}
📞 Aloqa:{malumotlar['Nomer']}
🌐 Hudud: {malumotlar['Manzil']}
💰 Narxi: {malumotlar['Narxi']}
👨🏻‍💻 Kasbi: {malumotlar['Kasb']}
🕰 Murojaat qilish vaqti: {malumotlar['Murojatvaqt']}
🔎 Maqsad:{malumotlar['Maqsad']}
""")
    await msg.answer("Barcha ma'lumotlar to'g'rimi", reply_markup=finish)