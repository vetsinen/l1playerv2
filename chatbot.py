import telebot
from telebot import types
import pathlib
from os import listdir
from random import randrange

bot = telebot.TeleBot("1093604140:AAGlTCUgzPSLZsJNrSDO_hrj54IGbveU7NU")  # token for @bailandobot

@bot.message_handler(commands=['track'])
def send_track(message: types.Message):
    bot.send_message(message.chat.id, 'ща пошлю')
    staticpath = str(pathlib.Path(__file__).parent.absolute()) + '/static/mp3/'
    files = [f for f in listdir(staticpath)]
    audio = files[randrange(len(files))]
    print(audio)
    # for origfile in files:
    with open("static/mp3/"+audio, "rb") as misc:
        f = misc.read()
    bot.send_audio(message.chat.id, f, timeout=10000)

@bot.message_handler(commands=['top'])
def send_welcome(message: types.Message):
    blackpool: str = ''' Самые горячие хиты 2020
Criminal
Con Calma
Corazón
Sax
Calma (Remix)
Soltera (Remix)
Que Tire Pa Lante
X ft. J Balvin
Chill Day
  '''
    bot.send_message(message.chat.id, blackpool)


@bot.message_handler(content_types=['text'])
def send_text(message: types.Message):
    if message.text.lower() == 'привіт':
        bot.send_message(message.chat.id, 'Привіт, ' + message.chat.username)
    elif message.text.lower() == 'прощавай':
        bot.send_message(message.chat.id, 'Прощавай, ' + message.chat.username)
    else:
        bot.send_message(message.chat.id, '¿Hablas español?')


if __name__ == '__main__':
    bot.polling()
