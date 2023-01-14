import telebot
import psycopg2
from config import *
from db_connect import db_conncet

def start_bot(token):
    bot = telebot.TeleBot(token)
    user_auth = False
    
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, f"Доброго времени суток {message.from_user.username}!\nВведите пароль...")

    # ВЫХОД ИЗ ПРОГИ, КОНЕЦ    
    @bot.message_handler(commands=['stop'])
    def start_message(message):
        user_auth = False
        bot.send_message(message.chat.id, f"Всего доброго! {message.from_user.username}!\n")

    # ПРОВЕРКА ПАРОЛЯ
    @bot.message_handler(content_types=['text'])
    def password_check(message):
        user_password = message.text

        if user_password == 'test':
            user_auth = True

            try:
                bot.send_message(message.chat.id, 'Доступ разрешен!')
                connect = psycopg2.connect(f'host={HOST} user={USER_DB} dbname={NAME_DB} password={user_password}')
                db_conncet(connect,bot,message)
            except Exception as ex:
                bot.send_message(message.chat.id,f"{'-'*20}\n[INFO] Ошибка программы!!!\n{ex}\n{'-'*20}\n")
        else:
            bot.send_message(message.chat.id, 'Пароль не верный!')

    bot.polling()

# НАЧАЛО
if __name__ == '__main__':
    # ЗАПУСК БОТА
    start_bot(TOKEN_BOT)