from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def build_reply_buttons(buttons , size):
    rkb = ReplyKeyboardBuilder()
    rkb.add(*buttons)
    rkb.adjust(*size)
    return rkb.as_markup(resize_keyboard=True)