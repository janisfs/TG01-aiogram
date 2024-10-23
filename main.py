import asyncio
from aiogram import (Bot, Dispatcher, executor
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, Я бот!")

async def on_startup(_):
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
