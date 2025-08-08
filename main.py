import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
import random

# from gtts import gTTS
# import os

from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.callback_query(F.data == 'more')
async def more(message: Message):
   await message.answer("Опции подгружены", reply_markup=kb.option)
   # await callback.message.edit_text('Опции подгружены', reply_markup=kb.option)

@dp.message(F.text == "Опция 1")
async def opt1_button(message: Message):
   await message.answer('Это текст первой опции')

@dp.message(F.text == "Опция 2")
async def opt2_button(message: Message):
   await message.answer('Это текст второй опции')

@dp.message(F.text == "Привет")
async def hi_button(message: Message):
   await message.answer(f'Привет, {message.from_user.first_name}!')

@dp.message(F.text == "Пока")
async def buy_button(message: Message):
   await message.answer(f'До свидания, {message.from_user.first_name}!')

@dp.message(Command('help'))
async def help(message: Message):
   await message.answer('Этот бот умеет выполнять команды: \n /start \n /help \n /links \n /dynamic')

@dp.message(Command('links'))
async def links(message: Message):
   await message.answer('Выберите, что Вас интересует:', reply_markup=kb.inline_keyboard_links)

@dp.message(Command('dynamic'))
async def links(message: Message):
   await message.answer('Выберите, что Вас интересует:', reply_markup=kb.inline_keyboard_dynamic)

@dp.message(CommandStart())
async def start(message: Message):
   await message.answer('Меню с кнопками находится ниже:', reply_markup=kb.main)

async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())