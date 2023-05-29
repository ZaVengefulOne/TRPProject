import random
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import Parser
import requests
from bs4 import BeautifulSoup

token = "6077834064:AAEi70eoSxqqIu9YC3eiuQKB2jM1XjP9sMI"
bot = Bot(token=token)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)
c = str(random.randint(1, 700))
url = "https://eda.ru/recepty?page=" + c
response = requests.get(url)

html_text = response.text
soup = BeautifulSoup(html_text, "html.parser")
recipes_list = soup.find_all(class_='emotion-1eugp2w')
hrefs = soup.find_all(class_='emotion-18hxz5k', href=True)


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




def random_recipe():
    # Получаем HTML-код страницы с помощью метода get(url)

    # if response.status_code == 200:
    #
    #     # print(html_text)
    # else:
    #     print('Ошибка:', response.status_code)
    #     html_text = 0

    # Парсинг HTML-кода и извлечение списка рецептов

    list = ""
    for i in range(len(recipes_list)):
        list += str(i + 1)
        list += ")"
        list += recipes_list[i].text
        list += "\n"
    #    print("\t(", hrefs[i]['href'], ")")
    list += "Введите номер рецепта (от 1 до {}): ".format(len(recipes_list))
    return list


def random_recipe2(choice):
    while True:
        recipe_url = "https://eda.ru" + hrefs[int(choice) - 1]['href']
        recipe_response = requests.get(recipe_url)
        recipe_html_text = recipe_response.text
        recipe_soup = BeautifulSoup(recipe_html_text, "html.parser")
        recipe_title = recipes_list[int(choice) - 1].text
        recipe_ingredients = recipe_soup.find_all(class_='emotion-mdupit')
        quantity_recipe_ingredients = recipe_soup.find_all(class_='emotion-bsdd3p')
        recipe_steps = recipe_soup.find_all(class_='emotion-1dvddtv')
        recipe_text = recipe_title + "\n"
        recipe_text += "Ингредиенты: \n"
        for i in range(len(recipe_ingredients)):
            ingredient = recipe_ingredients[i].text.strip()
            quantity = quantity_recipe_ingredients[i].text.strip()
            recipe_text += "- {} ({}) \n".format(ingredient, quantity)
        recipe_text += "Пошаговый рецепт: \n"
        for i, step in enumerate(recipe_steps):
            recipe_text += "\t{}. {} \n".format(i + 1, step.text.strip())
        return recipe_text



# def documentation():
#     i = 0
#     for methods in dir(Parser):
#         print(dir(Parser)[i], "--", eval("Parser." + methods + ".__doc__"))
#         i += 1


if __name__ == '__main__':
    executor.start_polling(dp)

