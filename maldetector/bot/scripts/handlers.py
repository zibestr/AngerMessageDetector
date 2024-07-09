from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

import bot.assets.text as text
from backends import MaliciousDetector

router = Router()
detector = MaliciousDetector('maldetector/model/support_vector.bin',
                             'maldetector/model/label_encoder.bin')


@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer(text.greet)


@router.message()
async def answer(msg: Message):
    answers = detector.inspect_urls(msg.text)
    if answers:
        answers_buttons = [
            [InlineKeyboardButton(text=f'Ссылка №{i} невредоностна',
                                  callback_data='wrong')]
            for i in range(1, len(answers) + 1)
        ]

        kb = InlineKeyboardMarkup(inline_keyboard=answers_buttons)
        await msg.answer('Результат:\n' + '\n'.join(answers),
                         reply_markup=kb)
    else:
        await msg.answer(text.not_detected_urls)


@router.callback_query(F.data == 'wrong')
async def wrong_label(msg: Message):
    await msg.answer(text.wrong_label)
