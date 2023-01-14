def db_conncet(connect,bot,message):
    try:
        connect.autocommit = True
        cur = connect.cursor()
        err_type = f"{'-'*20}\n[INFO]Не корректное значение\n{'-'*20}\n"

        # ВХОД В МЕНЮ
        while 1:
            try:
                bot.send_message(message.chat.id, '---МЕНЮ---\n' +
                    '/list - вывести список данных\n' +
                    '/date - внести/удалить данные\n' +
                    '/exit - выход'
                )
                break
                # if user_command == 1:
                #     # ВЫВОД СПИСКА
                #     list_output(cur)
                #     print()
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
                #     break 
                # else:
                #     print(err_type)
            except Exception as ex:
                bot.send_message(message.chat.id, err_type)
    except Exception as ex:
        bot.send_message(message.chat.id,f"{'-'*20}\n[INFO] Ошибка программы!!!\n{ex}\n{'-'*20}\n")