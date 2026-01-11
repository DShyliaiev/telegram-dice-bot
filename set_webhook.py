import asyncio
from aiogram import Bot
from config import BOT_TOKEN

WEBHOOK_URL = "https://telegram-dice-bot-8xkj.onrender.com/webhook"

async def main():
    bot = Bot(BOT_TOKEN)
    await bot.set_webhook(WEBHOOK_URL)
    print(f"Webhook установлен: {WEBHOOK_URL}")
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
