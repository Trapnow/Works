from aiogram import types, Router
from aiogram.filters import CommandStart

from keyboards.keybords import start_kb

router = Router()


@router.message(CommandStart())
async def handle_start(msg: types.Message):
    a = '''Я, Оксана Марьясова
Предметный & food фотограф📸
Стаж работы 4 года

Осуществляю профессиональную фотосъёмку товара или
услуги, тем самым представляю ваш продукт "вкусным" и
продаваемым, что несомненно, повышает прибыльность вашего бизнеса 📈💰💰💰

Тип услуг:
🔸Предметная съёмка для маркетплейса 
🔸Предметная съёмка для каталога и сайта, соц.сетей
🔸Фуд - съёмка для меню
🔸Контент съёмка 

Цена за фото - 350₽, если съёмка стекла - 450₽.'''
    await msg.answer(
        f"Hello, {msg.from_user.full_name}\n{a}",
        reply_markup=start_kb())
