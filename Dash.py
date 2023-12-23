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