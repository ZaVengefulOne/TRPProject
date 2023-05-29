import random

import requests
from bs4 import BeautifulSoup


def get_recipe(search):
    # Получаем HTML-код страницы с помощью метода get(url)
    url = "https://eda.ru/recipesearch?onlyEdaChecked=true&q=" + search
    response = requests.get(url)

    if response.status_code == 200:
        html_text = response.text
    else:
        return 'Ошибка при получении рецепта'

    # Парсинг HTML-кода и извлечение списка рецептов
    soup = BeautifulSoup(html_text, "html.parser")
    recipes_list = soup.find_all(class_='horizontal-tile__item-title item-title')
    hrefs = soup.find_all(class_='breadcrumbs', href=True)
    recipes = []
    link = []
    for i in range(len(recipes_list)):
        recipe = ''
        letter_flag = False
        for j in range(len(recipes_list[i].text)):
            if not letter_flag and recipes_list[i].text[j].isalpha():
                letter_flag = True
            if letter_flag:
                if recipes_list[i].text[j].isalpha() or recipes_list[i].text[j] == ' ' or recipes_list[i].text[j] == '\u00A0':
                    recipe += recipes_list[i].text[j]
        recipes.append(recipe)

        recipe_link = 'https://eda.ru'
        link_start = str(recipes_list[i]).find('href=') + 6
        link_iterator = link_start
        while True:
            if str(recipes_list[i])[link_iterator] == '"':
                break
            recipe_link += str(recipes_list[i])[link_iterator]
            link_iterator += 1
        link.append(recipe_link)

    # Поиск по запросу
    choice = 1  # Выбираем первый рецепт из списка

    recipe_url = link[choice - 1]
    recipe_response = requests.get(recipe_url)
    recipe_html_text = recipe_response.text
    recipe_soup = BeautifulSoup(recipe_html_text, "html.parser")
    recipe_title = recipes[choice - 1]
    recipe_ingredients = recipe_soup.find_all(class_='emotion-mdupit')
    quantity_recipe_ingredients = recipe_soup.find_all(class_='emotion-bsdd3p')
    recipe_steps = recipe_soup.find_all(class_='emotion-1dvddtv')

    # Формируем текст рецепта
    recipe_text = f'Рецепт для "{recipe_title}":\n\n'
    recipe_text += 'Ингредиенты:\n'
    for ingredient in recipe_ingredients:
        recipe_text += f'- {ingredient.text.strip()}\n'
    recipe_text += '\nПриготовление:\n'
    for i, step in enumerate(recipe_steps):
        recipe_text += f'{i+1}. {step.text.strip()}\n'

    return recipe_text

def recipe_search(search):
    # Парсинг HTML-кода и извлечение списка рецептов
    # Получаем HTML-код страницы с помощью метода get(url)
    url = "https://eda.ru/recipesearch?onlyEdaChecked=true&q=" + search
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    recipes_list = soup.find_all(class_='horizontal-tile__item-title item-title')
    hrefs = soup.find_all(class_='breadcrumbs', href=True)
    recipes = []
    link = []
    for i in range(len(recipes_list)):
        recipe = ''
        recipe_return = ""
        letter_flag = False
        for j in range(len(recipes_list[i].text)):
            if not letter_flag and recipes_list[i].text[j].isalpha():
                letter_flag = True
            if letter_flag:
                if recipes_list[i].text[j].isalpha() or recipes_list[i].text[j] == ' ' or recipes_list[i].text[j] == '\u00A0':
                    recipe += recipes_list[i].text[j]
        recipes.append(recipe)
        recipe_return += f"{i + 1}) {recipe}"
        return recipe_return


def recipe_search2(choice):
    recipes_list = soup.find_all(class_='horizontal-tile__item-title item-title')
    recipe_link = 'https://eda.ru'
    link_start = str(recipes_list[choice]).find('href=') + 6
    link_iterator = link_start
    while True:
        if str(recipes_list[choice])[link_iterator] == '"':
            break
        recipe_link += str(recipes_list[choice])[link_iterator]
        link_iterator += 1
    link.append(recipe_link)
    recipe_url = link[choice - 1]
    recipe_response = requests.get(recipe_url)
    recipe_html_text = recipe_response.text
    recipe_soup = BeautifulSoup(recipe_html_text, "html.parser")
    recipe_title = recipes
    recipe_ingredients = recipe_soup.find_all(class_='emotion-mdupit')
    quantity_recipe_ingredients = recipe_soup.find_all(class_='emotion-bsdd3p')
    recipe_steps = recipe_soup.find_all(class_='emotion-1dvddtv')
    print(recipes[choice - 1])
    print("Ингредиенты:")
    for i in range(len(recipe_ingredients)):
        ingredient = recipe_ingredients[i].text.strip()
        quantity = quantity_recipe_ingredients[i].text.strip()
        print("- {} ({})".format(ingredient, quantity))
    print("Пошаговый рецепт:")
    for i, step in enumerate(recipe_steps):
        print("\t{}. {}".format(i + 1, step.text.strip()))