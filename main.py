from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
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

# Этот хэндлер будет срабатывать на команду "/ahtung"    
@dp.message(Command(commands=["ahtung"]))
async def process_ahtyng_command(message:Message):
    api_photo = 'https://random.dog/woof.json'
    api_response=requests.get(api_photo)
    if api_response.status_code==200:
        photo_link = api_response.json()['url']
        await message.answer_photo(photo_link)
    else:
        await message.answer(ERROR_TEXT)

# Этот хэндлер будет срабатывать на команду "/valera"        
@dp.message(Command(commands=["valera"]))
async def process_valera_command(message:Message):
    api_photo = 'https://randomfox.ca/floof/'
    api_response=requests.get(api_photo)
    if api_response.status_code==200:
        photo_link = api_response.json()['image']
        await message.answer_photo(photo_link, caption='Вот такой Валера!')
    else:
        await message.answer(ERROR_TEXT)
        

# Этот хэндлер будет срабатывать на отправку фото
@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)       

#стикер
@dp.message(F.sticker)
async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)
    
# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд   
@dp.message(F.text)
async def send_text_echo(message: Message):
    await message.answer(text=message.text)

#аудио
@dp.message(F.audio)
async def send_audio_echo(message:Message):
    await message.answer("Аудио")

#гифки анимации
@dp.message(F.animation)
async def send_animation_echo(message:Message):
    await message.answer("message.animation.file_id")

#документы
@dp.message(F.document)
async def send_document_echo(message:Message):
    await message.answer("Документ")

#видео
@dp.message(F.video)
async def send_video_echo(message:Message):
    await message.answer("Видео")

#видео кружок    
@dp.message(F.video_note)
async def send_video_note_echo(message:Message):
    await message.answer("Видео заметка")

#голосовые сообщения    
@dp.message(F.voice)
async def send_voice_echo(message:Message):
    await message.answer("Голосовое")

#контакты    
@dp.message(F.contact)
async def send_contact_echo(message:Message):
    await message.answer("Контакт")

#Для всех не описаных типов
@dp.message()
async def send_any_echo(message:Message):
    await message.answer("Что то другое")

if __name__ == '__main__':
    dp.run_polling(bot)
