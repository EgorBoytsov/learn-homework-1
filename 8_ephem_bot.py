"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Привет')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def constellation(update, context):
    planets = {
        'Mercury': ephem.Mercury,
        'Venus': ephem.Venus,
        'Mars': ephem.Mars,
        'Jupiter': ephem.Jupiter,
        'Saturn': ephem.Saturn,
        'Uranus': ephem.Uranus,
        'Neptune': ephem.Neptune,
        'Pluto': ephem.Pluto,
        'Moon': ephem.Moon
    }

    user_text = update.message.text.split()[1].capitalize()

    if user_text in planets:
        planet = ephem.constellation(planets[user_text](date.today()))
    else:
        update.message.reply_text('Других планет я не знаю')


    update.message.reply_text(planet)


def main():
    mybot = Updater(settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
