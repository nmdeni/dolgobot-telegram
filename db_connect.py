def db_conncet(connect,bot,message):
    connect.autocommit = True
    cur = connect.cursor()
    err_type = f"{'-'*20}\n[INFO]Не корректное значение\n{'-'*20}\n"

    # ВХОД В МЕНЮ
    bot.send_message(message.chat.id, '---МЕНЮ---\n' +
        '/list - вывести список данных\n' +
        '/date - внести/удалить данные\n' +
        '/exit - выход'
    )

    @bot.message_handler(content_types=['text'])
    def list_show(message):
        # if message.text == '/list':
            # ВЫВОД СПИСКА
        bot.send_message(message.chat.id, 'Вот список')
        # elif user_command == 2:
        #     # ДОБАВЛЕНИЕ/УДАЛЕННИЕ ДАННЫХ
        #     user_command2 = int(input('\n1 - внести\n2 - удалить\n3 - выход\n-> '))
            
        #     if user_command2 == 1:
        #         insert_db(cur)
        #     elif user_command2 == 2:
        #         delDateDb(cur)
        #     elif user_command2 == 3:
        #         continue
        #     else:
        #         print(err_type)
        #         continue
        # elif user_command == 3:
        # else:
        #     bot.send_message(message.chat.id, 'Нет такой команды!')