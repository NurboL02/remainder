from aiogram import types
from configure import scheduler, bot


async def start_reminder(message: types.Message):
    scheduler.add_job(
        send_reminder,
        'interval',
        days=2,
        args=(message.from_user.id,)
    )
    await message.answer("В душ каждые 2 дня!")


async def send_reminder(user_id: int):
    await bot.send_message(
        chat_id=user_id,
        text="Сегодня надо принять душ"
    )
