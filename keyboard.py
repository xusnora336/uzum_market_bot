from aiogram.types import  KeyboardButton, ReplyKeyboardMarkup,WebAppInfo



btn_keyboard=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kompaniya xaqida"),
         KeyboardButton(text="menyu",web_app=WebAppInfo(url="")])