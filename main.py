import telebot
import random
from telebot import types

bot = telebot.TeleBot("2082683437:AAFG_jlZkPfZGzyXCPFP0LHOlOUPoesMWas")
secret_numbers = {}

def number_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    markup.row(
        types.KeyboardButton('1'),
        types.KeyboardButton('2'),
        types.KeyboardButton('3')
    )
    markup.row(
        types.KeyboardButton('4'),
        types.KeyboardButton('5'),
        types.KeyboardButton('6')
    )
    markup.row(
        types.KeyboardButton('7'),
        types.KeyboardButton('8'),
        types.KeyboardButton('9')
    )
    return markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "guesse the number from 1 to 9")
    bot.send_message(message.chat.id, "guesse the number ", reply_markup=number_keyboard())

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_id = message.chat.id
    guessed_number = None
    if chat_id in secret_numbers:
        guessed_number = secret_numbers[chat_id]
    else:
        guessed_number = random.randint(1,9)
        secret_numbers[chat_id] = guessed_number

    reply_number = int(message.text)
    if  guessed_number>reply_number:
        bot.send_message(chat_id, f"my number is larger than {reply_number}")
    elif guessed_number<reply_number:
        bot.send_message(chat_id, f"my number is lower than{reply_number}")
    else:
        bot.send_message(chat_id, f"u win my number is{reply_number}")
    bot.send_message(chat_id, "guesse the number ", reply_markup=number_keyboard())

bot.infinity_polling()