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
