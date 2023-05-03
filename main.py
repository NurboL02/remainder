from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import text, italic, bold, spoiler
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)



@dp.message_handler(commands=["start",])
async def start(message: types.Message):
    # print(dir(message.from_user))
    first_name = message.from_user.first_name
    id = message.from_user.id
    await message.answer(f"Приветствуем тебя, пользователь {first_name}, {id}")
@dp.message_handler(commands=["pic"])
async def picture(message: types.Message):
    with open('image_tg/car.jpg', 'rb') as photo:
        await message.reply_photo(
            photo,
            caption="the red car"
        )
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Это эхо бот и может отправлять рандомные фотки через /pic \n и знает информацию о вас /my_info ")
@dp.message_handler(commands=['my_info'])
async def send_welcome(message: types.Message):
    firstname = message.from_user.first_name
    await message.reply(
        text(
            "здравстуй",
            italic("твое имя"),
            bold(firstname),

            spoiler(f"твой id{message.from_user.id}")
        ),
        parse_mode="MarkdownV2"
    )
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)



if __name__ == "__main__":
    executor.start_polling(dp)