import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

import keyboard
from keyboard import btn
BOT_TOKEN = getenv("BOT_TOKEN")
load_dotenv()
dp = Dispatcher()   


@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Uzum market botiga xush kelibsz",reply_markup=btn)


# Run the bot
async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Starting bot...")

    asyncio.run(main())