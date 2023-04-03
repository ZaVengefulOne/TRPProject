# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
#
# token = "6077834064:AAEi70eoSxqqIu9YC3eiuQKB2jM1XjP9sMI"
# bot = Bot(token=token)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands=['start' , 'help'])
# async def send_welcome(msg: types.message):
#     await msg.reply_to_message(f'Привет, я - бот помощник повара. Приятно познакомиться, {msg.from_user.full_name}')
#
#
# @dp.message_handler(content_types=['text'])
# async def get_text_messages(msg: types.Message):
#    if msg.text.lower() == 'привет':
#        await msg.answer('Привет!')
#    else:
#        await msg.answer('Не понимаю, что это значит.')
# test
# if __name__ == '__main__':
#     executor.start_polling(dp)

