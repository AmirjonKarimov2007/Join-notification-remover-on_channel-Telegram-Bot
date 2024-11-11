from aiogram import Bot, Dispatcher, types
from loader import dp,bot
from keyboards.inline.boglanish_button import startkeyboard
from aiogram.types import ParseMode

@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def handle_new_chat_members(message: types.Message):
    await message.delete()

    text = f"<b>Assalomu alaykum <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>. @Amirjon_Karimov_Blog kanaling muhokama guruhiga xush kelibsiz!Men bilan ishlash uchun.</b>"
    await message.answer(text=text, parse_mode=ParseMode.HTML, reply_markup=startkeyboard)

@dp.message_handler(content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
async def handle_left_chat_member(message: types.Message):
    await message.delete()