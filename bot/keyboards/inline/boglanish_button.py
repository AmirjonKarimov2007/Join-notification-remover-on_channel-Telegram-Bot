from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
check = InlineKeyboardMarkup(row_width=2)

check.insert(InlineKeyboardButton(text="✅Ha", callback_data='ha'))
check.insert(InlineKeyboardButton(text="❌Yo'q", callback_data='Yoq'))

startkeyboard = InlineKeyboardMarkup(row_width=2)
startkeyboard.insert(InlineKeyboardButton(text="✅Fiverr",url='fiverr.com/amirjonkarimov'))
startkeyboard.insert(InlineKeyboardButton(text="📹You tube",url='https://www.youtube.com/@AmirjonKarimovBlog'))
# startkeyboard.insert(InlineKeyboardButton(text="🌐Web site",url='fiverr.com/amirjonkarimov'))
startkeyboard.insert(InlineKeyboardButton(text="🔰Linkedin",url='https://www.linkedin.com/in/amirjon-karimov'))