from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
from keyboards.client_kb import *
import random
from parser_wheel.parser_wheel import parser

async def send_audio(message: types.Message):
    audios = (
        'media/50_Cent_x_Скриптонит_x_Andy_Panda_Привычка_Kerim_Remix_.mp3',
        'media/RMR-DEALER-feat-Future-Lil-Baby-Official-Music-Video.m4a',
        'media/Su x Worth It [BADAYTOFF TIK TOK EDIT].mp3',
        'media/Врываемся.mp3',
        'media/Скриптонит_x_Truwer_Животные_edit_by_8kenshi.mp3',
    )
    audio = open(random.choice(audios), 'rb')
    await bot.send_audio(message.chat.id, audio=audio)
async def parsser_wheels(message: types.Message):
    items = parser()
    for item in items:
        await bot.send_message(
            message.from_user.id,

            f"{item['link']}"
            f"{item['logo']}\n"
            f"# {item['size']}\n"
            f"цена - {item['price']}\n"
            )
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "Кто лучший препод?"
    answer = [
        "Airas",
        "Bekbolot",
        "Esen",
        "igor",
        "Nurlan",
        "Aleksey",
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )


async def start_command(message: types.Message):
    await message.answer('Hello bro!', reply_markup=start_markup)


async def help_command(message: types.Message):
    await message.answer('Сам разбирайся брат!')


async def mem_command(message: types.Message):
    photos = (
        'media/mem1.htm',
        'media/mem2.htm',
        'media/mem3.htm',
    )
    photo = open(random.choice(photos), 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


async def pin_chat_command(message: types.Message):
    if message.chat.type != 'private':
        if message.reply_to_message:
            await bot.pin_chat_message(message.chat.id, message_id=message.reply_to_message.message_id)
        else:
            await message.answer('сообщение должно быть ответом')
    else:
        await message.answer('пиши в группе')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem_command, commands=['mem'])
    dp.register_message_handler(send_audio, commands=['music'])
    dp.register_message_handler(parsser_wheels, commands=['wheel'])
    dp.register_message_handler(pin_chat_command, commands=['pin'], commands_prefix='!')
