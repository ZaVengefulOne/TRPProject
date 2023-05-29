import random

import requests
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from bs4 import BeautifulSoup

import SearchParser
import Parser

token = "6077834064:AAEi70eoSxqqIu9YC3eiuQKB2jM1XjP9sMI"
bot = Bot(token=token)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)
url = "https://eda.ru/recepty"



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.message):
    chat_id = msg.chat.id
    await msg.reply(f'Привет, я - бот помощник повара. Приятно познакомиться, {msg.from_user.full_name}')
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🔍Поиск"),
                KeyboardButton(text="📃Случайный"),
            ]
        ],
        resize_keyboard=True
    )
    # Отправляем клавиатуру пользователю
    await bot.send_message(chat_id=chat_id, text="Выберите команду:", reply_markup=keyboard)


@dp.message_handler(Text("🔍Поиск"))  # обрабатываем команду /recipe
async def get_recipe(msg: types.Message):
    chat_id = msg.chat.id
    await bot.send_message(chat_id=chat_id,text="Введите блюдо, которые вы хотите найти")
    @dp.message_handler()
    async def recipe(msg: types.Message):
        search = msg.text
        recipe = Parser.get_recipe(search)
        if recipe:
            await msg.answer(recipe)  # отправляем рецепт пользователю
        else:
            await msg.answer('Рецепт не найден')  # отправляем сообщение об ошибке

    # search = msg.text.split('/recipe ')[1]  # получаем запрос пользователя
    #   # вызываем функцию из Parser и получаем результат
    #


@dp.message_handler(Text("📃Случайный"))
async def handle_message(msg: types.Message):
    # Отправляем пользователю случайный рецепт
    await msg.answer(SearchParser.random_recipe())

    @dp.message_handler()
    async def handle_message2(msg: types.Message):
        choice = msg.text
        await msg.answer(SearchParser.random_recipe2(choice))


def documentation():
    i = 0
    for methods in dir(Parser):
        print(dir(Parser)[i], "--", eval("Parser." + methods + ".__doc__"))
        i += 1


if __name__ == '__main__':
    executor.start_polling(dp)
    # documentation()
