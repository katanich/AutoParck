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