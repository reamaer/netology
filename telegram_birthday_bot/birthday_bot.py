from config import TOKEN
import telebot
from datetime import datetime

token = TOKEN
bot = telebot.TeleBot(token)


def tick():
    message = 'Tick! The time is: %s' % datetime.now()
    return message


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, str(tick()))


bot.polling(none_stop=True)
