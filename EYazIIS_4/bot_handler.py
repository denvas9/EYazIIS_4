import random

import telebot
import os
import json
import text_analyze.dictionary
import text_analyze.worldcloud
import text_analyze.check_books
from help_texts.help import HELPTEXT
from help_texts.help_wordcloud import HELPCLOUD
from help_texts.main_help import MAINHELP


bot = telebot.TeleBot("5271283143:AAEt2SvRMo1X4TcXuqPJZ8xxPvgnkXbam1A")
bot_command_key = dict()
path = os.getcwd()

bot_choose_book_key = False
bot_choose_snack_key = False
get_snack = False

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


def get_snack_answer():
    with open(os.getcwd() + '/dialog_handler/snackDialog.txt', encoding='utf-8') as file:
        price = random.randint(30, 99)
        data = ''
        for line in file:
            choose = random.randint(0, 1)
            print(choose)
            if 'клетку' in data.lower() and choose != 0:
                yield f'Отличный выбор! Тетрадь в клетку будет стоить {price} коп.'
            elif 'линейку' in data.lower() and choose != 0:
                yield f'Отличный выбор! Тетрадь в линейку будет стоить {price} коп.'
            elif 'косую линейку' in data.lower() and choose != 0:
                yield f'Отличный выбор! Тетрадь в косую линейку будет стоить {price} коп.'

            data = yield line


snack_answer = get_snack_answer()


@bot.message_handler(content_types=['text'])
def send_text(message):
    global bot_command_key
    global bot_choose_book_key
    global bot_choose_snack_key
    global get_snack
    key = False
    if 'форму' in message.text.lower():
        key = True
        bot_command_key[message.chat.id] = 'форма'
        bot.send_message(message.chat.id, HELPTEXT)
    elif 'синоним' in message.text.lower():
        key = True
        bot_command_key[message.chat.id] = 'слово'
        bot.send_message(message.chat.id, HELPCLOUD)
    elif 'книгу' in message.text.lower() and 'выбрать' in message.text.lower():
        key = True
        bot_command_key[message.chat.id] = 'книга'
        bot.send_message(message.chat.id, "Какой жанр в книгах ты предпочитаешь?")

    if not key and message.chat.id in bot_command_key and len(bot_command_key[message.chat.id]) > 0:
        if bot_command_key[message.chat.id] == 'форма':
            answer = text_analyze.dictionary.generate_form(message.text)
            bot.send_message(message.chat.id, "Твое слово это: " + answer)
        elif bot_command_key[message.chat.id] == 'слово':
            bot.send_photo(message.chat.id, text_analyze.worldcloud.semantic_analysis(message.text))
        elif bot_command_key[message.chat.id] == 'книга':
            bot.send_message(message.chat.id, "Я нашел прекрасный выбор для тебя!")
            bot.send_photo(message.chat.id, text_analyze.check_books.find_books(message.text))
            bot_choose_book_key = True
        bot_command_key[message.chat.id] = ''
    elif bot_choose_snack_key is True:
        if message.text.lower() == 'нет':
            bot_choose_snack_key = False
            bot.send_message(message.chat.id, sorry_answer)
        else:
            answer = snack_answer.send(message.text.lower())
            if 'клетку' in answer.lower():
                bot.send_message(message.chat.id, answer)
                get_snack = True
                bot_choose_snack_key = False
            elif 'линейку' in answer.lower():
                bot.send_message(message.chat.id, answer)
                get_snack = True
                bot_choose_snack_key = False
            elif 'косую линейку' in answer.lower():
                bot.send_message(message.chat.id, answer)
                get_snack = True
                bot_choose_snack_key = False
            else:
                bot.send_message(message.chat.id, answer)

    elif 'купить' in message.text.lower() and 'тетрадку' in message.text.lower():
        if not get_snack:
            bot_choose_snack_key = True
            bot.send_message(message.chat.id, snack_answer.send(None))
        else:
            bot.send_message(message.chat.id, "You already have chosen snacks.")
    elif not key:
        bot_choose_snack_key = False
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

keyboard = telebot.types.ReplyKeyboardMarkup(True, True, True, True)
keyboard.row('Помоги мне создать форму русского слова')
keyboard.row('Помоги мне создать синоним')
keyboard.row('Помоги мне выбрать книгу')
keyboard.row('Помоги мне купить тетрадку')
