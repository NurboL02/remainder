
from aiogram import executor
from aiogram.dispatcher.filters import Text
from configure import dp, scheduler
import logging

from remainder import start_reminder

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Напоминалка
    dp.register_message_handler(start_reminder, commands=["rem"])

    # этот обработчик обрабатывает все сообщения поэтому он ниже всех
    scheduler.start()
    executor.start_polling(dp)
