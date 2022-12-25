from telebot import TeleBot, types
import os
from calc import calc

os.chdir(os.path.dirname(__file__))

TOKEN = '5917885348:AAHOQHN4LEGoc2zjou4D0Aco57Qg13PTCNo'

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_menu(msg: types.Message):
    keyboard = types.ReplyKeyboardMarkup(True)
    menu = ('1. Калькулятор.', '2. Записная книжка.',
            '3. Крестики-Нолики.', '4. Конфетный Король.')
    keyboard.row(*menu)
    bot.send_message(chat_id=msg.from_user.id,
                     text='Привет! Что выберешь?\n{}\n{}\n{}\n{}'.format(*menu), reply_markup=keyboard)


@bot.message_handler()
def answer(msg: types.Message):
    text = msg.text
    menu_dict = {'1. Калькулятор.': (
        calc.calculator, 'Введите математическое выражение:', answer1)}
    keys = [*menu_dict.keys()]
    el1, el2, el3 = 0, 0, 0
    for key in keys:
        if text in key:
            el1, el2, el3 = menu_dict[key]
            bot.send_message(chat_id=msg.from_user.id, text=f'{el2}')
            bot.register_next_step_handler(msg, el3)


def answer1(msg):
    result = calc.calculator(msg.text)
    bot.send_message(chat_id=msg.from_user.id, text=f'{msg.text}={result}')


bot.polling()