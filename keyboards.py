from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def cube_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="U", callback_data="U"),
            InlineKeyboardButton(text="D", callback_data="D"),
            InlineKeyboardButton(text="L", callback_data="L"),
            InlineKeyboardButton(text="R", callback_data="R"),
            InlineKeyboardButton(text="F", callback_data="F"),
            InlineKeyboardButton(text="B", callback_data="B"),
        ],
        [
            InlineKeyboardButton(text="🔀 Shuffle", callback_data="shuffle")
        ]
    ])
