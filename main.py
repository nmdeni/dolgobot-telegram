import telebot
import psycopg2
from config import *
from listDb import list_output
from readDb import readDB

def reset_user_ins():
    global user_ins,read_ins_activ,read_menu_activ
    user_ins = {
        'name':'',
        'sum':'',
        'status':''
    }
    read_ins_activ = False
    read_menu_activ = False
    
user_auth = False
cur = {}
read_menu_activ = False
read_del_activ = False
read_ins_activ = False
user_ins = {
    'name':'',
    'sum':'',
    'status':''
}
ins_command_use = ''
main_menu_text = '---МЕНЮ---\n'+ '/list - вывести список данных\n'+'/date - внести/удалить данные\n'+'/exit - выход'

def start_bot(token):
    bot = telebot.TeleBot(token)
    
    @bot.message_handler(commands=['start'])
    def start_message(message):
        global user_auth
        
        if user_auth:
            bot.send_message(message.chat.id, 'Вы подключены')
        else:
            bot.send_message(message.chat.id, f"Доброго времени суток {message.from_user.username}!\nВведите пароль...")

    # ВЫХОД ИЗ ПРОГИ, КОНЕЦ    
    @bot.message_handler(commands=['stop'])
    def stop_message(message):
        global user_auth
        user_auth = False
        bot.send_message(message.chat.id, f"Всего доброго! {message.from_user.username}!\n")

    
    @bot.message_handler(content_types=['text'])
    def password_check(message):
        global user_auth,cur,read_menu_activ,read_del_activ,read_ins_activ,user_ins,ins_command_use
            
        if message.text == 'test' and user_auth != True:
            user_auth = True
            user_password = message.text

            try:
                bot.send_message(message.chat.id, 'Доступ разрешен!\n' + main_menu_text)
                connect = psycopg2.connect(f'host={HOST} user={USER_DB} dbname={NAME_DB} password={user_password}')
                connect.autocommit = True
                cur = connect.cursor()
                err_type = f"{'-'*20}\n[INFO]Не корректное значение\n{'-'*20}\n"
                return

            except Exception as ex:
                bot.send_message(message.chat.id,f"{'-'*20}\n[INFO] Ошибка программы!!!\n{ex}\n{'-'*20}\n")

        elif user_auth != True:
            bot.send_message(message.chat.id, 'Неверный пароль')

        if user_auth and read_menu_activ == False and message.text == '/list':
            bot.send_message(message.chat.id, list_output(cur,DB_TABLE))
        elif user_auth and read_menu_activ == False and message.text == '/date':
            read_menu_activ = True
            return bot.send_message(message.chat.id, '/ins - добавить'+'\n'+'/del - удалить')
        elif user_auth and read_menu_activ == False and message.text == '/exit':
            stop_message(message)
        elif user_auth and read_menu_activ == False:
            bot.send_message(message.chat.id, 'Нет такой комманды!!!')

        # DEL -----------------
        if read_menu_activ and message.text == '/del':
            bot.send_message(message.chat.id, 'Введите ID удаления (пример - 0)')
            read_del_activ = True
        elif read_menu_activ and read_del_activ:
            try:
                bot.send_message(message.chat.id,readDB(cur, DB_TABLE, '/del', item=int(message.text)) 
                    + main_menu_text
                )
                read_menu_activ = False
                read_del_activ = False

            except Exception as ex:
                bot.send_message(message.chat.id,f"{'-'*20}\n[INFO] Неверное значение!!!\n{ex}\n{'-'*20}\n"
                    + main_menu_text
                )
                read_menu_activ = False 
                read_del_activ = False
        # -----------------

        # INS -----------------
        if read_menu_activ and (message.text == '/ins' or ins_command_use == 'ins_name'):
            read_ins_activ = True
            ins_command_use = 'input_name'
            bot.send_message(message.chat.id, 'Введите имя')
            return
        if read_ins_activ and user_ins['name'] == '' and ins_command_use == 'input_name':
            user_ins['name'] = message.text
            ins_command_use = 'ins_sum'

        if user_ins['name'] != '' and read_ins_activ and ins_command_use == 'ins_sum':
            bot.send_message(message.chat.id, f"Имя - {user_ins['name']}")
            bot.send_message(message.chat.id, 'Введите сумму')
            ins_command_use = 'input_sum'
            return
        if read_ins_activ and user_ins['sum'] == '' and ins_command_use == 'input_sum':
            try:
                user_ins['sum'] = int(message.text)
                ins_command_use = 'ins_status'
            except Exception as ex:
                reset_user_ins()
                bot.send_message(message.chat.id, 'Вы ввели не число!!!\n'+main_menu_text)
                return

        if user_ins['sum'] != '' and read_ins_activ and ins_command_use == 'ins_status':
            bot.send_message(message.chat.id, f"Имя - {user_ins['name']}\nСумма - {user_ins['sum']}")
            bot.send_message(message.chat.id, 'Введите статус \n(1 - вы должны, 0 - вам)')
            ins_command_use = 'input_status'
            return
        if read_ins_activ and user_ins['status'] == '' and ins_command_use == 'input_status':
            if message.text == '1':
                user_ins['status'] = 'true'
                bot.send_message(message.chat.id,readDB(cur, DB_TABLE, '/ins', user_ins) 
                    + main_menu_text
                )
                reset_user_ins()
                return
            elif message.text == '0':
                user_ins['status'] = 'false'
                bot.send_message(message.chat.id,readDB(cur, DB_TABLE, '/ins', user_ins) 
                    + main_menu_text
                )
                reset_user_ins()
                return
            else:
                reset_user_ins()
                bot.send_message(message.chat.id, 'Некорректное значение!!!\n'+main_menu_text)
                return

        # -----------------


        
        

    bot.polling()

# НАЧАЛО
if __name__ == '__main__':
    # ЗАПУСК БОТА
    start_bot(TOKEN_BOT)