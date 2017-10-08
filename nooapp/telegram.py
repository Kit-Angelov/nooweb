# -*- coding: utf-8 -*-
import telebot

BOT_TOKEN = '453272136:AAGOYUmlzWI2poAO6kBw1Oac7xFxwsq2ubo'
CHANNEL_NAME = '@nootech'
chat_id = '-1001114206508'

bot = telebot.TeleBot(BOT_TOKEN)


def send_telegram(date, name='нема имени', phone='нема телефона', message='нема сообщения'):
    msg = 'Т. {0}\n{1}\nИмя: {2}\n{3}'.format(str(phone), str(date), str(name), str(message))
    bot.send_message(chat_id, msg)
