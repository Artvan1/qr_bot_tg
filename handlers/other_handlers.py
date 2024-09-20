# my_bot/handlers.py
from aiogram import Router
from aiogram.types import Message
from aiogram.types import FSInputFile
from fanc_bot.qr_code import generate_qr_from_number
from lexicon.lexicon import LEXICON_RU


# Создание роутера
router = Router()



# Обработчик текстовых сообщений
@router.message()
async def handle_message(message: Message):
    text = message.text
    if text.isdigit():
        file_path = 'qr_code.png'
        generate_qr_from_number(text, file_path)
        qr_code = FSInputFile(file_path)
        await message.answer_photo(photo=qr_code)
    else:
        await message.answer(text=LEXICON_RU['no_digit'])
