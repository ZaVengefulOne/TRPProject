from aiogram import Bot, types
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.utils import executor

import Parser

token = "6077834064:AAEi70eoSxqqIu9YC3eiuQKB2jM1XjP9sMI"
bot = Bot(token=token)
dp = Dispatcher(bot)
url = "https://eda.ru/recepty"


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.message):
    await msg.reply(f'Привет, я - бот помощник повара. Приятно познакомиться, {msg.from_user.full_name}')


@dp.message_handler(commands=['recipe'])  # обрабатываем команду /recipe
async def get_recipe(msg: types.Message):
    search = msg.text.split('/recipe ')[1]  # получаем запрос пользователя
    recipe = Parser.get_recipe(search)  # вызываем функцию из Parser и получаем результат
    if recipe:
        await msg.answer(recipe)  # отправляем рецепт пользователю
    else:
        await msg.answer('Рецепт не найден')  # отправляем сообщение об ошибке


@dp.message_handler(commands=['random'])
async def handle_message(msg: types.Message):
    await msg.answer(Parser.random_recipe())


def documentation():
    i = 0
    for methods in dir(Parser):
        print(dir(Parser)[i], "--", eval("Parser." + methods + ".__doc__"))
        i += 1


if __name__ == '__main__':
    executor.start_polling(dp)
    # documentation()
