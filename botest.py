import telebot
from telebot import types
import requests

bot_token = "6326697207:AAEHuZBH9kMeVwj3djFLFnJr6VWYTONaKaw"
bot = telebot.TeleBot(bot_token)

car_list = {
    'Легковые': ['Lexus', 'BMW', 'Mercedes-Benz'],
    'Грузовые': ['Тягач', 'Открытый кузов', 'Спец техника'],
}
requests = {}

@bot.message_handler(commands=['start'])
def send_menu(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1) # Указываем ширину строки кнопок
    rent_button = types.KeyboardButton('Аренда авто')
    help_button = types.KeyboardButton('Помощь')
    charts_button = types.KeyboardButton('Диаграмма BPMN')
    shorts_button = types.KeyboardButton('Дашборд')
    keyboard.add(rent_button, help_button, charts_button, shorts_button)

    bot.send_message(message.chat.id, 'Выберите пункт меню:', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Аренда авто")
def rent_car(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "добро пожаловать! чтобы создать заявку, выберите тип авто из списка:")

    # вывод списка доступных марок авто
    keyboard = types.InlineKeyboardMarkup()
    for car in car_list.keys():
        button = types.InlineKeyboardButton(text=car, callback_data=car)
        keyboard.add(button)

    bot.send_message(chat_id, "выберите марку авто:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data in car_list.keys())
def car_selection(call):
    chat_id = call.message.chat.id
    car = call.data

    # сохранение выбранной марки авто в заявке
    requests[chat_id] = {'car': car}

    # вывод списка доступных моделей для выбранной марки авто
    keyboard = types.InlineKeyboardMarkup()
    for model in car_list[car]:
        button = types.InlineKeyboardButton(text=model, callback_data=model)
        keyboard.add(button)

    bot.send_message(chat_id, "выберите модель авто:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data in car_list[requests[call.message.chat.id]['car']])
def model_selection(call):
    chat_id = call.message.chat.id
    model = call.data

    # сохранение выбранной модели авто в заявке
    requests[chat_id]['model'] = model

    bot.send_message(chat_id, "выберите дату использования авто (dd/mm/yyyy):")


@bot.message_handler(regexp=r'\d{2}/\d{2}/\d{4}')
def date_selection(message):
    chat_id = message.chat.id
    date = message.text

    # сохранение выбранной даты в заявке
    requests[chat_id]['date'] = date

    bot.send_message(chat_id, "заявка создана, приезжайте в компанию за авто!")


@bot.message_handler(func=lambda message: message.text == "просмотр заявки")
def edit_request(message):
    chat_id = message.chat.id

    if chat_id in requests:
        request = requests[chat_id]
        car = request['car']
        model = request['model']
        date = request['date']
        bot.send_message(chat_id, f"ваша заявка:\nмарка авто: {car}\nмодель авто: {model}\nдата: {date}")
    else:
        bot.send_message(chat_id, "у вас нет активных заявок.")

@bot.message_handler(func=lambda message: message.text == 'Помощь')
def help_menu(message):
    submenu_keyboard = types.ReplyKeyboardMarkup(row_width=1)
    edit_request_button = types.KeyboardButton('просмотр заявки')
    contact_operator_button = types.KeyboardButton('связаться с оператором')
    submenu_keyboard.add(edit_request_button, contact_operator_button)

    bot.send_message(message.chat.id, 'выберите действие:', reply_markup=submenu_keyboard)


@bot.message_handler(func=lambda message: message.text == "связаться с оператором")
def edit_request(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Позвоните к нам в контору +79XXXXXXXXX ")




# Добавленная кнопка
@bot.message_handler(func=lambda message: message.text == 'Дашборд')
def shorts_button(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    dashboardOp_button = types.KeyboardButton('Что такое Дашборд')
    dashboard1_button = types.KeyboardButton('Dashboard 1')
    dashboard2_button = types.KeyboardButton('Dashboard 2')
    dashboard3_button = types.KeyboardButton('Dashboard 3')
    dashboard4_button = types.KeyboardButton('Dashboard 4')
    dashboard5_button = types.KeyboardButton('Dashboard 5')
    dashboard6_button = types.KeyboardButton('Dashboard 6')
    back_button = types.KeyboardButton('назад')
    keyboard.add( dashboardOp_button, dashboard1_button, dashboard2_button, dashboard3_button, dashboard4_button, dashboard5_button,
                 dashboard6_button, back_button)

    bot.send_message(message.chat.id, 'Выберите дашборд:', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'назад')
def show_dashboard1(message):
    bot.send_message(message.chat.id,'/start')



@bot.message_handler(func=lambda message: message.text == 'Что такое Дашборд')
def show_dashboard1(message):
    bot.send_message(message.chat.id,
                     'Дашборд предназначен для визуализации и анализа данных о загружености сервиса в определнное время. '
                     'Содержит пять ключевых графиков, о загружености сервиса в определнное время.')
    pass

@bot.message_handler(func=lambda message: message.text == 'Dashboard 1')
def show_dashboard1(message):
    image1_url = 'https://raw.githubusercontent.com/katanich/AutoParck/development/Point.jpg'
    bot.send_photo(message.chat.id, image1_url, caption='Это точечный график')
    pass


@bot.message_handler(func=lambda message: message.text == 'Dashboard 2')
def show_dashboard2(message):
    image1_url = 'https://raw.githubusercontent.com/katanich/AutoParck/development/Stolb.jpg'
    bot.send_photo(message.chat.id, image1_url, caption='Это столбчатый график')
    pass


@bot.message_handler(func=lambda message: message.text == 'Dashboard 3')
def show_dashboard3(message):
    image1_url = 'https://raw.githubusercontent.com/katanich/AutoParck/development/krug.jpg'
    bot.send_photo(message.chat.id, image1_url, caption='Это круговой график')
    pass


@bot.message_handler(func=lambda message: message.text == 'Dashboard 4')
def show_dashboard4(message):
    image1_url = 'https://raw.githubusercontent.com/katanich/AutoParck/development/Line.jpg'
    bot.send_photo(message.chat.id, image1_url, caption='Это линейный график')
    pass


@bot.message_handler(func=lambda message: message.text == 'Dashboard 5')
def show_dashboard5(message):
    image1_url = 'https://raw.githubusercontent.com/katanich/AutoParck/development/Yachik.jpg'
    bot.send_photo(message.chat.id, image1_url, caption='Это ящичковый график')
    pass


@bot.message_handler(func=lambda message: message.text == 'Dashboard 6')
def show_dashboard6(message):
    image1_url = 'https://raw.githubusercontent.com/katanich/AutoParck/development/table.jpg'
    bot.send_photo(message.chat.id, image1_url, caption='Это таблица')
    pass

@bot.message_handler(func=lambda message: message.text == 'Диаграмма BPMN')
def help_menu(message):
    submenu_keyboard = types.ReplyKeyboardMarkup(row_width=1)
    edit_request_button = types.KeyboardButton('Описание')
    contact_operator_button = types.KeyboardButton('Ссылка на схему BPMN')
    OP_operator_button = types.KeyboardButton('Что такое дабшорд')
    submenu_keyboard.add(edit_request_button, OP_operator_button, contact_operator_button)

    bot.send_message(message.chat.id, 'выберите действие:', reply_markup=submenu_keyboard)

@bot.message_handler(func=lambda message: message.text == 'Описание')
def show_dashboard1(message):
    bot.send_message(message.chat.id,
                     'Диаграммы BPMN (Business Process Model and Notation) представляют собой стандартный '
                         'графический язык, разработанный для моделирования бизнес-процессов в организации. '
                         'Этот инструмент обеспечивает единый и понятный способ визуализации бизнес-процессов, '
                         'что помогает более эффективно понимать, анализировать и оптимизировать деятельность компании')
    pass


@bot.message_handler(func=lambda message: message.text == 'Ссылка на схему BPMN')
def show_dashboard1(message):
    image1_url = 'https://raw.githubusercontent.com/katanich/AutoParck/feature/Диаграмма с ТГ(1).jpg'
    bot.send_photo(message.chat.id, image1_url, caption='Это изображение BPMN по управлению заявками на аренду авто')
    pass

@bot.message_handler(func=lambda message: message.text == 'Что такое Дашборд')
def show_dashboard1(message):
    bot.send_message(message.chat.id,
                     'Дашборд предназначен для визуализации и анализа данных о загружености сервиса в определнное время. '
                     'Содержит пять ключевых графиков, о загружености сервиса в определнное время.')
    pass
bot.polling(non_stop=True)