# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime




# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}



# Запись отчета о работе бота
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot_2.log'
                    )



# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    commands = ['start', 'list', 'planet']  # коммандное меню бота
    mybot = Updater('670738456:AAHvJ361jqkFts55DbjuH36nfcmdRL-4wc4', request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler(commands, processing_com_and_constellation))
    mybot.start_polling()
    mybot.idle()




#в функции задан словарь со список планет(ephem_planets) из модуля ephem, в переменной reply -
#написаны команды для меню и список планет при обращении к команде (/list)
def processing_com_and_constellation(bot,update):
    ephem_planets = {
            "Mercury" : ephem.Mercury,
            "Venus" : ephem.Venus,
            "Mars" : ephem.Mars,
            "Jupiter" : ephem.Jupiter,
            "Saturn" : ephem.Saturn,
            "Uranus" : ephem.Uranus,
            "Neptune" : ephem.Neptune,
            "Pluto" : ephem.Pluto,
            "Moon" : ephem.Moon,
            }
    reply = {"/start": "Welcome!\n Commands:\n /start - Start bot \n /planet - Planet \n /list - Planet list",
              "/list": "Planets list: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Moon",
              "/planet": "At {} planet {} is in the constellation {}",

            }
    command = update.message.text.split()


    if command[0] == "/planet" and len(command) < 2:
        update.message.reply_text("You must choose planet! Example: /planet  Mars") #

    elif command[0] == "/planet" and len(command) == 2:
        planet_name = command[1].capitalize()
        planet = ephem_planets.get(planet_name)
        if planet:
            full_name = ephem.constellation(planet(datetime.date.today()))
        else:
            update.message.reply_text("There is no planet in a list!")
        update.message.reply_text(reply.get(command[0]).format(datetime.date.today(), planet_name, full_name))
    else:
        update.message.reply_text(reply.get(command[0]))


#запускает бота
main()