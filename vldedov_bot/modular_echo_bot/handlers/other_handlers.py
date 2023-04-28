from aiogram.types import Message
from aiogram import Router
from modular_echo_bot.lexicon.lexicon import LEXICON_RU

# Инициализируем роутер уровня модуля
router: Router = Router()

@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except:
        await message.reply(text=LEXICON_RU['no_echo'])