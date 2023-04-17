import random

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN: str = '5849642826:AAFOvnJTbn1sDvVO7cT4HcV1K8Lxo08cIk8'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()

@dp.message(Command(commands=['start']))
async def process_start_command(message:Message):
    await message.answer(text='Это комманда start')

if __name__ == '__main__':
    dp.run_polling(bot)