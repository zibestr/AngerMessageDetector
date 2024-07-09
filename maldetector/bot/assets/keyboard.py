from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup
)


menu_buttons = [
    [InlineKeyboardButton(text="", callback_data="help"),
     InlineKeyboardButton(text="Ссылка невредоностна", callback_data="balance")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Меню", callback_data="menu")]])
