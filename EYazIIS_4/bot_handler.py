import random
import os
import json
import telebot

import text_analyze.check_films
import text_analyze.website
import text_analyze.check_books

from help_texts.main_help import MAINHELP


bot = telebot.TeleBot("5271283143:AAEt2SvRMo1X4TcXuqPJZ8xxPvgnkXbam1A")
bot_command_key = dict()
path = os.getcwd()

#bot_command_video=False
#bot_command_site=False
#bot_command_book=False

sorry_answer = 'Извини, я не могу тебе помочь'


def get_dialogs():
    with open(os.getcwd() + '/dialog_handler/dialog.json', 'r', encoding='utf-8') as file:
        data = file.read().strip()
    return json.loads(data)

@bot.message_handler(commands=['start'])
def start_message_handler(message):
    bot.send_message(message.chat.id, 'Привет, могу я тебе как-то помочь?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help_message_handler(message):
    bot.send_message(message.chat.id, MAINHELP, reply_markup=keyboard)



@bot.message_handler(content_types=['text'])
def send_text(message):

    global bot_command_key

  #  global bot_command_video
  #  global bot_command_site
  #  global bot_command_book

    key = False

    if 'видео' in message.text.lower():
       # bot_command_video = True
      #  key=True
        bot_command_key[message.chat.id] = 'видео'
        bot.send_message(message.chat.id, "Ну, сейчас что-нибудь подберу...")
    elif 'книгу' in message.text.lower():
        key=True
       # bot_command_book = True
        bot_command_key[message.chat.id] = 'книга'
        bot.send_message(message.chat.id, "Хочешь найти что-нибудь о генетике, анатомии или что-то общее?")
    elif 'сайт' in message.text.lower():
       # key=True
       # bot_command_site = True
        bot_command_key[message.chat.id] = 'сайт'
        bot.send_message(message.chat.id, "Ну, сейчас посмотрю что есть интересного...")



    if not key and message.chat.id in bot_command_key and len(bot_command_key[message.chat.id]) > 0:
        if bot_command_key[message.chat.id] == 'видео':
            answer = text_analyze.check_films.get_video()
            bot.send_message(message.chat.id, f"Вот, есть такое:{answer}")
        #    bot_command_video = False
            
        elif bot_command_key[message.chat.id] == 'книга':
            bot.send_message(message.chat.id, "Вот, нашёл кое что:")
            bot.send_photo(message.chat.id, text_analyze.check_books.find_books(message.text))
        #    bot_command_book = True

        elif bot_command_key[message.chat.id] == 'сайт':
            answer = text_analyze.website.get_site()
            bot.send_message(message.chat.id, f"Вот, есть такой сайт:{answer}")
         #   bot_command_site = False

        #сброс
        bot_command_key[message.chat.id] = ''
       # key=False

    elif not key:
        #Просто случайные ответы
        dialogs = get_dialogs()
        answer_key = False
        for dialog in dialogs:
            if message.text.lower() in dialog['question'].lower():
                answer_key = True
                answers = list(dialog['answer'].split('|'))
                bot.send_message(message.chat.id, answers[random.randint(0, len(answers) - 1)])
                break
        if answer_key is False:
            bot.send_message(message.chat.id, sorry_answer)

keyboard = telebot.types.ReplyKeyboardMarkup(True, True, True)

keyboard.row('Помоги мне найти интересный сайт')
keyboard.row('Помоги мне найти какое-нибудь видео о природе')
keyboard.row('Помоги мне подобрать интересную книгу')
