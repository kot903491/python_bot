from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon_ru import LEXICON_RU
import requests

# Инициализируем роутер уровня модуля
router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(Command(commands='valera'))
async def process_valera_command(message: Message):
    valera_response = requests.get('https://randomfox.ca/floof/')
    if valera_response.status_code == 200:
        valera_link = valera_response.json()['image']
        await message.answer_photo(valera_link)
    else:
        await message.answer(text='Валера не выйдет')
