from aiogram.types import  KeyboardButton, ReplyKeyboardMarkup,WebAppInfo

btn=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kompaniya haqida"),
         KeyboardButton(text="Menyu",web_app=WebAppInfo(url="https://uzum.uz/")),],
        [KeyboardButton(text="Kontakt/Manzil"),],
    ],resize_keyboard=True,
)
