from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton("NEXT", callback_data="button_2")
    question = "Сколько областей в Кыргызстане?"
    markup.add(button_2)
    answer = [
        "12",
        "3",
        "7",
        "0",
        "-10",
        "999",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )

async def quiz_3(call: types.CallbackQuery):
    question = "сколько вам будет лет если вы родились бы 9 лет назад?"
    answer = [
        '10',
        '9',
        '5',
        '2',
        '5',
    ]


    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Стыдно не знать",
        # open_period=5,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
    dp.register_callback_query_handler(quiz_3, text="button_2")