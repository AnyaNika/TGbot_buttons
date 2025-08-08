from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
], resize_keyboard=True)

inline_keyboard_links = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", url='https://ria.ru/')],
   [InlineKeyboardButton(text="Музыка", url='https://music.yandex.ru/')],
   [InlineKeyboardButton(text="Видео", url='https://rutube.ru/')]
])

inline_keyboard_dynamic = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше", callback_data='more')]
])

option = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Опция 1"), KeyboardButton(text="Опция 2")]
], resize_keyboard=True)



#
# test = ["кнопка 1", "кнопка 2"]
#
# async def test_keyboard():
#    keyboard = InlineKeyboardBuilder()
#    for key in test:
#        keyboard.add(InlineKeyboardButton(text=key, url='https://www.youtube.com/watch?v=HfaIcB4Ogxk'))
#    return keyboard.adjust(2).as_markup()