from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


def start_kb():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Начать!")]
            ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return kb

def type_photo_kb():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Каталожная")],
            [KeyboardButton(text="Композиционная")]
            ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return kb


def background_color_kb():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Тёмный")],
            [KeyboardButton(text="Светлый")]
            ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return kb


