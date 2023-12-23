import telebot
from telebot import types
import requests

@bot.message_handler(commands=['start'])
def send_menu(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1) # Указываем ширину строки кнопок
    rent_button = types.KeyboardButton('Аренда авто')
    help_button = types.KeyboardButton('Помощь')
    charts_button = types.KeyboardButton('Диаграмма BPMN')
    shorts_button = types.KeyboardButton('Дашборд')
    keyboard.add(rent_button, help_button, charts_button, shorts_button)

    bot.send_message(message.chat.id, 'Выберите пункт меню:', reply_markup=keyboard)