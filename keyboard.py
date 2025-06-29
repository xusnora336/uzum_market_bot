from aiogram.types import  KeyboardButton, ReplyKeyboardMarkup,WebAppInfo

btn=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kompaniya haqida"),
         KeyboardButton(text="Menyu",web_app=WebAppInfo(url="https://xusnora336.github.io/uzum_market_bot/")),],
        [KeyboardButton(text="Filliallar",web_app=WebAppInfo(url="""https://www.google.com/maps/search/uzum+filiallari/@41.3087608,69.2368698,13z?entry=ttu&g_ep=EgoyMDI1MDYwOS4wIKXMDSoASAFQAw%3D%3D""")),
         KeyboardButton(text="Bo'sh ish o'rinlari",web_app=WebAppInfo(url="""https://uzum.uz/uz/about/careers?srsltid=AfmBOorIdGnWfDVDKagGynBO23vYKdd5WaDWCAK4tenO0Yb_HN1dRQKR"""))],
        [KeyboardButton(text="Tilni tanlash"),]
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
         KeyboardButton(text="Меню",web_app=WebAppInfo(url="https://xusnora336.github.io/uzum_market_bot/")),],
        [KeyboardButton(text="Филиалы",web_app=WebAppInfo(url="""https://www.google.com/maps/search/uzum+filiallari/@41.3087608,69.2368698,13z?entry=ttu&g_ep=EgoyMDI1MDYwOS4wIKXMDSoASAFQAw%3D%3D""")),
         KeyboardButton(text="Вакансии",web_app=WebAppInfo(url="""https://uzum.uz/uz/about/careers?srsltid=AfmBOorIdGnWfDVDKagGynBO23vYKdd5WaDWCAK4tenO0Yb_HN1dRQKR"""))],
        [KeyboardButton(text="Выбор языка")],
    ],resize_keyboard=True,
)

btn_en=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="About the company"),
         KeyboardButton(text="Menu",web_app=WebAppInfo(url="https://xusnora336.github.io/uzum_market_bot/")),],
        [KeyboardButton(text="Branches",web_app=WebAppInfo(url="""https://www.google.com/maps/search/uzum+filiallari/@41.3087608,69.2368698,13z?entry=ttu&g_ep=EgoyMDI1MDYwOS4wIKXMDSoASAFQAw%3D%3D""")),
         KeyboardButton(text="Job openings",web_app=WebAppInfo(url="""https://uzum.uz/uz/about/careers?srsltid=AfmBOorIdGnWfDVDKagGynBO23vYKdd5WaDWCAK4tenO0Yb_HN1dRQKR"""))],
        [KeyboardButton(text="Language selection")],
    ],resize_keyboard=True,
)

