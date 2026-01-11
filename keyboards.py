from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def dice_keyboard():

    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎲 Бросить кубик", callback_data="roll_dice")]
    ])
