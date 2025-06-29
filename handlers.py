import os

from aiogram import Dispatcher, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, FSInputFile
from keyboard import btn, tilni_tanlash, btn_ru, btn_en


router = Router()

@router.message(F.text=="Kompaniya haqida")
async def Kompaniya(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "uzum.png"))
    text="""Uzum Market – Oʻzbekistonda faoliyat olib borayotgan eng katta marketpleyslardan biri.
Marketpleys ilovasi 2023-yil davomida 13,5 milliondan ortiq
Telegram va Instagram tarmoqlari ilovalaridan keyingi eng koʻp yuklab olingan uchinchi ilova boʻldi"""
    await message.answer_photo(photo=img,caption=text,reply_markup=btn)

@router.message(F.text=="Tilni tanlash")
async def til(message: Message):
    text="Tilni tanlang"
    await message.answer(text,reply_markup=tilni_tanlash)

@router.message(F.text=="🇺🇿")
async def uz(message: Message):
    text="Siz O'zbek tilini tanladingiz"
    await message.answer(text,reply_markup=btn)

@router.message(F.text=="🇷🇺")
async def ru(message: Message):
    text="Вы выбрали русский язык"
    await message.answer(text,reply_markup=btn_ru)
@router.message(F.text=="🇺🇸")
async def en(message: Message):
    text="You have chosen the Russian language"
    await message.answer(text,reply_markup=btn_en)

@router.message(F.text=="О компании")
async def okompanii(message: Message):
    img=FSInputFile(os.path.join(os.path.dirname(__file__), "images", "uzum.png"))
    text="""Uzum Market-один из крупнейших действующих в Узбекистане маркетплейсов.
Приложение Marketpleys имеет более 13,5 миллионов пользователей в течение 2023 года
Telegram и Instagram стали третьим по загруженности приложением после сетевых приложений"""
    await message.answer_photo(caption=text,photo=img,reply_markup=btn_ru)

@router.message(F.text=="Выбор языка")
async def yazik(message: Message):
    text="Выберите язык"
    await message.answer(text,reply_markup=tilni_tanlash)

@router.message(F.text=="About the company")
async def company(message: Message):
    img=FSInputFile(os.path.join(os.path.dirname(__file__), "images", "uzum.png"))
    text="""Uzum Market is one of the largest trading platforms operating in Uzbekistan.
In 2023, the Marketpleys app was visited by over 13.5 million users.
Telegram and Instagram have become the third busiest apps after online ones."""
    await message.answer_photo(caption=text,photo=img,reply_markup=btn_en)

@router.message(F.text=="Language selection")
async def language(message: Message):
    text="Select a language"
    await message.answer(text,reply_markup=tilni_tanlash)

