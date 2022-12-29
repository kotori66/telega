import telebot
from telebot import types

import requests


TOKEN = 'Token_API'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    """Функия отвечающая на команды 'help' и 'start'"""
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    cat_btn = types.KeyboardButton('кота😺')
    dog_btn = types.KeyboardButton('собаку🐶')
    markup.add(cat_btn, dog_btn)
    bot.send_message(message.chat.id, """\
Этот бот умеет скидывать котов и собак.
Жми на соответствующие кнопки и будет счастье:)\
""", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_photo(message):
    """Фунция отправляет фото на запрос пользователя"""
    # если отправлена собака или кошка возвращается соответствующая картинка
    if message.text.strip() == 'кота😺':
        bot.send_photo(message.chat.id, photo_cat())
    elif message.text.strip() == 'собаку🐶':
        bot.send_photo(message.chat.id, photo_dog())
    else:
        bot.send_message(message.chat.id, f'Я не знаю, что такое {message.text}, так что')
        frog = open('frog.png', 'rb')
        bot.send_photo(message.chat.id, frog)


def photo_cat():
    """Парсинг и возвращение картинок котов"""
    response_cat = requests.get('https://api.thecatapi.com/v1/images/search')
    return response_cat.json()[0]['url']


def photo_dog():
    """Парсинг и возвращение картинок собак"""
    response_dog = requests.get('https://api.thedogapi.com/v1/images/search')
    return response_dog.json()[0]['url']


if __name__ == '__main__':
    bot.infinity_polling()
