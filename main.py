import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Не понятно, что это может быть!', 'Я не знаю, что это такое!', 'Не отправляйте мне такое больше!', 'Круто!', 'Это очень красивое фото!']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)

@dp.message(Command("photo"))
async def photo(message: Message):
    list = ['https://i.pinimg.com/236x/93/ed/3a/93ed3af6411e1e8b997038c74c287a8a.jpg', 'https://ic.pics.livejournal.com/olegmakarenko.ru/12791732/2404737/2404737_original.jpg',
            'Не отправляйте мне такое больше!', 'Круто!', 'Это очень красивое фото!']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Ого, какая фотка!')

@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')


@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("Привет! Я бот, который может отправлять новости. Вот мои команды:\n"
                         "/news - Получить последнюю новость\n"
                         "/help - Получить список команд")


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, Я бот!")

async def on_startup(_):
    await dp.start_polling(bot)

async def main():
    await on_startup(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


# my_pal_bot
# best_pal_bot
