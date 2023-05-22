from aiogram import Bot, types
from aiogram.dispatcher.dispatcher import Dispatcher
import Parser
token = "6077834064:AAEi70eoSxqqIu9YC3eiuQKB2jM1XjP9sMI"
bot = Bot(token=token)
dp = Dispatcher(bot)
url = "https://eda.ru/recepty"


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.message):
    await msg.reply_to_message(f'Привет, я - бот помощник повара. Приятно познакомиться, {msg.from_user.full_name}')


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text.lower() == 'привет':
        await msg.answer('Привет!')
    else:
        await msg.answer('Не понимаю, что это значит.')


def documentation():
    i = 0
    for methods in dir(Parser):
        print(dir(Parser)[i], "--", eval("Parser." + methods + ".__doc__"))
        i += 1


if __name__ == '__main__':
    # executor.start_polling(dp)
    documentation()
