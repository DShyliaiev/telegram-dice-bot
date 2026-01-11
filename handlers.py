from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
import asyncio
from keyboards import dice_keyboard

router = Router()

# Команда /start
@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет! 🎲 Я бот для игры с кубиком.\n"
        "Нажми кнопку ниже или введи команду /dice",
        reply_markup=dice_keyboard()
    )

# Команда /dice (текстом)
@router.message(Command("dice"))
async def dice_text(message: Message):
    dice_msg = await message.answer_dice()
    await asyncio.sleep(3)  # ждём анимацию
    value = dice_msg.dice.value
    await message.answer(f"🎯 Выпало число: <b>{value}</b>")

# Кнопка
@router.callback_query(lambda c: c.data == "roll_dice")
async def dice_button(query: CallbackQuery):
    await query.answer()  # убираем часики на кнопке
    dice_msg = await query.message.answer_dice()
    await asyncio.sleep(3)
    value = dice_msg.dice.value
    await query.message.answer(f"🎯 Выпало число: <b>{value}</b>")
