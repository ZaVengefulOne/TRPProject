import requests
from bs4 import BeautifulSoup

# Получаем HTML-код страницы с помощью метода get(url)
url = "https://eda.ru/recepty"
response = requests.get(url)

if response.status_code == 200:
    html_text = response.text
    # print(html_text)
else:
    print('Ошибка:', response.status_code)
    html_text = 0

# Парсинг HTML-кода и извлечение списка рецептов
soup = BeautifulSoup(html_text, "html.parser")
recipes_list = soup.find_all(class_='emotion-1eugp2w')
hrefs = soup.find_all(class_='emotion-18hxz5k', href=True)

for i in range(len(recipes_list)):
    print(i+1,")", recipes_list[i].text)
#    print("\t(", hrefs[i]['href'], ")")

while True:
    choice = int(input("Введите номер рецепта (от 1 до {}): ".format(len(recipes_list))))

    if choice < 1 or choice > len(recipes_list):
        print("Неверный ввод. Попробуйте еще раз.")

    recipe_url = "https://eda.ru" + hrefs[choice - 1]['href']
    recipe_response = requests.get(recipe_url)

    if recipe_response.status_code == 200:
        recipe_html_text = recipe_response.text
    else:
        print('Ошибка:', recipe_response.status_code)
        recipe_html_text = 0

    recipe_soup = BeautifulSoup(recipe_html_text, "html.parser")
    recipe_title = recipes_list[choice-1].text
    recipe_ingredients = recipe_soup.find_all(class_='emotion-mdupit')
    quantity_recipe_ingredients = recipe_soup.find_all(class_='emotion-bsdd3p')
    recipe_steps = recipe_soup.find_all(class_='emotion-wdt5in')

    print("Рецепт \"{}\"".format(recipe_title))
    print("Ингредиенты:")
    for i in range(len(recipe_ingredients)):
        ingredient = recipe_ingredients[i].text.strip()
        quantity = quantity_recipe_ingredients[i].text.strip()
        print("- {} ({})".format(ingredient, quantity))
    print("Пошаговый рецепт:")
    for i, step in enumerate(recipe_steps):
        print("\t{}. {}".format(i + 1, step.text.strip()))
    break