from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from googletrans import Translator

import app.keyboards as kb
from app.keyboards import create_user_link_markup
import app.database.requests as rq


router = Router()
translator = Translator()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Hello! You wrote a translator to the bot.\n'
                         'How can I help?\n'
                         '(To understand my functions call: /help)')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("/start - we are starting our cooperation\n"
                         "/give_dict - i'll give you your dictionary with translations\n"
                         "you can write other message and i'm translate it")


@router.message(Command('give_dict'))
async def cmd_dict(message: Message):
    u_id = message.from_user.id
    user_link_markup = create_user_link_markup(u_id)
    await message.reply("Link to your dictionary", reply_markup=user_link_markup)


@router.message()
async def translate_message(message: Message):
    text_to_translate = message.text
    translated_text = translator.translate(text_to_translate, dest='en').text  # en
    await rq.save_to_database(message.text, translated_text, message.from_user.id)
    await message.reply(f"Translated to en: \n{translated_text}")





"""
@router.message(Command('give_dict'))
async def cmd_dict(message: Message):
    u_id = message.from_user.id
    #функция которая принимает u_id и отдаёт ссылку на html страницу(на странице должны быть все слова u)
    #create_user_link_markup(u_id)
    await message.answer("Link to your dictionary", reply_markup=kb.dict_button)
"""















