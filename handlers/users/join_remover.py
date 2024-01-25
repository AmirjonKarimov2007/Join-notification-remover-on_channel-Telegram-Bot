from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from loader import dp,bot
GROUP_CHAT_ID = -1001802064035  # Replace with your actual group chat ID


@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def handle_new_chat_members(message: types.Message):
    # Delete join notification
    await message.delete()

@dp.message_handler(content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
async def handle_left_chat_member(message: types.Message):
    # Delete left group notification
    await message.delete()

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
