import telebot
import requests
import json

from  telebot import types 
with open("questions.json", 'r', encoding='UTF-8') as j:
                global contents
                contents = json.loads(j.read())


token = '1732352983:AAEW7rVJf74uc7wZrenNDI-_gbQLbAdnGp8'
bot = telebot.TeleBot(token)


rightAnsw = 0
keyboard = types.ReplyKeyboardMarkup() 
keyboard.row('/start')
@bot.message_handler(commands=['start'])

def start_handler(m):
	keyboard = types.ReplyKeyboardMarkup() 
	keyboard.row('Перейти к квизу', 'Узнать, кто создатель')
	send = bot.send_message(m.from_user.id, 'Добро пожаловать в programming quiz!\nВыберите на клавиатуре то, что вы хотите сделать.', reply_markup = keyboard)
	bot.register_next_step_handler(send, start_handler_01)

def correct(m):
    keyboard = types.ReplyKeyboardMarkup() 
    bot.send_message(m.from_user.id, 'Верно!', reply_markup = keyboard)

def wrong(m):
    keyboard = types.ReplyKeyboardMarkup() 
    bot.send_message(m.from_user.id, 'Неверно.', reply_markup = keyboard)

def start_handler_01(m):
	keyboard = types.ReplyKeyboardMarkup()
	if m.text == 'Перейти к квизу':
            global lst
            lst = ['1958','1955','1963']
            keyboard.row(*lst)
            bot.send_message(m.from_user.id, "Итак, первый вопрос:", reply_markup = keyboard)
            send = bot.send_message(m.from_user.id, contents['questionList']['1'], reply_markup = keyboard)
            bot.register_next_step_handler(send, start_handler_02)
	elif m.text == 'Узнать, кто создатель':
		bot.send_message(m.from_user.id, '@blessmemary', reply_markup = keyboard)

def start_handler_02(m):
    global rightAnsw
    keyboard = types.ReplyKeyboardMarkup() 
    if m.text == '1958':
            wrong(m)
            keyboard.row('Продолжить')
    elif m.text == '1955':
            correct(m)
            keyboard.row('Продолжить')
            rightAnsw+=1
    elif m.text == '1963':
            wrong(m)
            keyboard.row('Продолжить')
    send = bot.send_message(m.from_user.id, 'Продолжаем!', reply_markup = keyboard)
    bot.register_next_step_handler(send, start_handler_03)

def start_handler_03(m):
    global lst
    keyboard = types.ReplyKeyboardMarkup() 
    lst = ["Деннис Ритчи", "Роб Пайк", "Гвидо ван Россум"]
    keyboard.row(*lst)
    bot.send_message(m.from_user.id, "Второй вопрос:", reply_markup = keyboard)
    send = bot.send_message(m.from_user.id, contents['questionList']['2'], reply_markup = keyboard)
    bot.register_next_step_handler(send, start_handler_04)
    

def start_handler_04(m):
    global rightAnsw
    keyboard = types.ReplyKeyboardMarkup() 
    if m.text == 'Деннис Ритчи':
            wrong(m)
            keyboard.row('Продолжить')
    elif m.text == 'Гвидо ван Россум':
            correct(m)
            keyboard.row('Продолжить')
            rightAnsw+=1
    elif m.text == 'Роб Пайк':
            wrong(m)
            keyboard.row('Продолжить')
    send = bot.send_message(m.from_user.id, 'Продолжаем!', reply_markup = keyboard)
    bot.register_next_step_handler(send, start_handler_05)

def start_handler_05(m):
    global lst
    keyboard = types.ReplyKeyboardMarkup() 
    lst = ["16", "10", "8"]
    keyboard.row(*lst)
    bot.send_message(m.from_user.id, "Переходим к третьему вопросу:", reply_markup = keyboard)
    send = bot.send_message(m.from_user.id, contents['questionList']['3'], reply_markup = keyboard)
    bot.register_next_step_handler(send, start_handler_06)

def start_handler_06(m):
    global rightAnsw
    keyboard = types.ReplyKeyboardMarkup() 
    if m.text == '8':
            wrong(m)
            keyboard.row('Продолжить')
    elif m.text == '16':
            correct(m)
            keyboard.row('Продолжить')
            rightAnsw+=1
    elif m.text == '10':
            wrong(m)
            keyboard.row('Продолжить')
    send = bot.send_message(m.from_user.id, 'Продолжаем!', reply_markup = keyboard)
    bot.register_next_step_handler(send, start_handler_07)

def start_handler_07(m):
    global lst
    keyboard = types.ReplyKeyboardMarkup() 
    lst = ["8", "64", "0.125"]
    keyboard.row(*lst)
    bot.send_message(m.from_user.id, "Четвертый вопрос:", reply_markup = keyboard)
    send = bot.send_message(m.from_user.id, contents['questionList']['4'], reply_markup = keyboard)
    bot.register_next_step_handler(send, start_handler_08)

def start_handler_08(m):
    global rightAnsw
    keyboard = types.ReplyKeyboardMarkup() 
    if m.text == '8':
            wrong(m)
            keyboard.row('Продолжить')
    elif m.text == '0.125':
            correct(m)
            keyboard.row('Продолжить')
            rightAnsw+=1
    elif m.text == '64':
            wrong(m)
            keyboard.row('Продолжить')
    send = bot.send_message(m.from_user.id, 'Продолжаем!', reply_markup = keyboard)
    bot.register_next_step_handler(send, start_handler_09)

def start_handler_09(m):
    global lst
    keyboard = types.ReplyKeyboardMarkup() 
    lst = ["Правда", "Ложь"]
    keyboard.row(*lst)
    bot.send_message(m.from_user.id, "Финальный вопрос:", reply_markup = keyboard)
    send = bot.send_message(m.from_user.id, contents['questionList']['5'], reply_markup = keyboard)
    bot.register_next_step_handler(send, start_handler_10)

def start_handler_10(m):
    global rightAnsw
    keyboard = types.ReplyKeyboardMarkup() 
    if m.text == 'Правда':
            wrong(m)
            keyboard.row('Закончить квиз.')
    elif m.text == 'Ложь':
            correct(m)
            keyboard.row('Закончить квиз.')
            rightAnsw+=1
    bot.send_message(m.from_user.id, f'Спасибо за участие в квизе! Ваш результат {rightAnsw} правильных ответов из 5.', reply_markup = keyboard)
    rightAnsw = 0
bot.polling()
