import requests
from bs4 import BeautifulSoup

url = "https://eda.ru/recepty"
response = requests.get(url) # Получаем HTML-код страницы с помощью метода get(url)

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
    print(recipes_list[i].text)
    print(hrefs[i]['href'])
