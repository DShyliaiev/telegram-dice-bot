from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
import asyncio

router = Router()

@router.message(Command("dice"))
async def roll_dice(message: Message):
    dice_msg = await message.answer_dice()  # 🎲 3D-анимация
    await asyncio.sleep(3)                  # ждём анимацию
    value = dice_msg.dice.value             # число 1–6

    await message.answer(f"🎯 Зіграла цифра: <b>{value}</b>")
