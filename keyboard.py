from aiogram.types import  KeyboardButton, ReplyKeyboardMarkup,WebAppInfo

btn=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kompaniya haqida"),
         KeyboardButton(text="Menyu",web_app=WebAppInfo(url="https://uzum.uz/")),],
        [KeyboardButton(text="Tilni tanlash")],
    ],resize_keyboard=True,
)

tilni_tanlash=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿"),
         KeyboardButton(text="🇷🇺"),
         KeyboardButton(text="🇺🇸")]
    ],resize_keyboard=True,
)

btn_ru=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="О компании"),
         KeyboardButton(text="Меню",web_app=WebAppInfo(url="https://uzum.uz/")),],
        [KeyboardButton(text="Выбор языка")],
    ],resize_keyboard=True,
)

btn_en=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="About the company"),
         KeyboardButton(text="Menu",web_app=WebAppInfo(url="https://uzum.uz/")),],
        [KeyboardButton(text="Language selection")],
    ],resize_keyboard=True,
)

