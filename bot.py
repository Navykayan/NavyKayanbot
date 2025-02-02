import os
import random
import time
from telegram.ext import Updater, CommandHandler

# Получаем токен из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text('Привет! Я бот для показа времени и шуток. Вот мои команды:\n'
                              '/start - Приветственное сообщение\n'
                              '/time - Время в Москве и Новосибирске\n'
                              '/joke - Получить смешную цитату')

def time(update, context):
    from datetime import datetime
    import pytz

    # Москва
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%H:%M:%S')

    # Новосибирск
    novosibirsk_tz = pytz.timezone('Asia/Novosibirsk')
    novosibirsk_time = datetime.now(novosibirsk_tz).strftime('%H:%M:%S')

    update.message.reply_text(f'Время в Москве: {moscow_time}\n'
                              f'Время в Новосибирске: {novosibirsk_time}')

def joke(update, context):
    jokes = [
        "Я никогда не забываю лицо, но в твоём случае я сделаю исключение.",
        "Я не ленивый. Я просто в экономном режиме.",
        "Если вы думаете, что никто не любит вас, попробуйте не заплатить налог с дохода."
    ]
    update.message.reply_text(random.choice(jokes))

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('time', time))
    dispatcher.add_handler(CommandHandler('joke', joke))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
