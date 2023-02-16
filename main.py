from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import requests

api_response = requests.Response
ERROR_TEXT = 'Тут должна быть картинка :('

API_TOKEN:str = '5849642826:AAFOvnJTbn1sDvVO7cT4HcV1K8Lxo08cIk8'
bot:Bot = Bot(token=API_TOKEN)
dp:Dispatcher=Dispatcher()

@dp.message(Command(commands=["start"]))
async def process_start_command(message:Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')
    
# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')
    
@dp.message(Command(commands=["ahtung"]))
async def process_ahtyng_command(message:Message):
    api_photo = 'https://random.dog/woof.json'
    api_response=requests.get(api_photo)
    if api_response.status_code==200:
        photo_link = api_response.json()['url']
        await message.answer_photo(photo_link)
    else:
        await message.answer(ERROR_TEXT)
        
@dp.message(Command(commands=["valera"]))
async def process_valera_command(message:Message):
    api_photo = 'https://randomfox.ca/floof/'
    api_response=requests.get(api_photo)
    if api_response.status_code==200:
        photo_link = api_response.json()['image']
        await message.answer_photo(photo_link, caption='Вот такой Валера!')
    else:
        await message.answer(ERROR_TEXT)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
