import telebot
from config import *

def start_bot(token):
    bot = telebot.TeleBot(token)
    
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, f"Доброго времени суток {message.from_user.username}!\nВведите пароль...")

    # ВЫХОД ИЗ ПРОГИ, КОНЕЦ    
    @bot.message_handler(commands=['stop'])
    def start_message(message):
        bot.send_message(message.chat.id, f"Всего доброго! {message.from_user.username}!\n")

    # ПРОВЕРКА ПАРОЛЯ
    @bot.message_handler(content_types=['text'])
    def password_check(message):
        user_password = message.text

        if user_password == 'test':
            bot.send_message(message.chat.id, 'Доступ разрешен!')
        else:
            bot.send_message(message.chat.id, 'Пароль не верный!')
        # ########################################################################


    bot.polling()

# НАЧАЛО
if __name__ == '__main__':
    # ЗАПУСК БОТА
    start_bot(token_bot)