from aiogram import types, F, Router, Bot

from aiogram.fsm.context import FSMContext

from data.database import add_order, NewOrder
from keyboards.keybords import background_color_kb, type_photo_kb

router = Router()


@router.message(F.text == 'Начать!')
async def go_start(msg: types.Message, state: FSMContext):
    await state.set_state(NewOrder.name)
    await msg.answer(
        "Какую продукцию Вы хотите сфотографировать?"
    )


@router.message(F.text.casefold().in_(["каталожная", "композиционная"]), NewOrder.type)
async def go_kom_start(msg: types.Message, state: FSMContext):
    await state.update_data(type=msg.text)
    await state.set_state(NewOrder.num_one)
    await msg.answer(
        "Кол-во фотографий для одного предмета"
    )


@router.message(F.text.regexp(r"^(89|\+7)"), NewOrder.phone)
async def go_white_start(msg: types.Message, state: FSMContext):
    await state.update_data(phone=msg.text)
    data = await state.get_data()
    await add_order(data)
    await msg.answer(
        "Спасибо за Ваш заказ 💌 !!! С Вами свяжуться в течении суток!"
    )
    await state.clear()


@router.message(F.text.func(lambda msg: msg.isdigit()), NewOrder.num_one)
async def go_up(msg: types.Message, bot: Bot, state: FSMContext):
    await state.update_data(num_one=msg.text)
    await state.set_state(NewOrder.background)
    await msg.answer(
        "Съемка придметов на светлом фоне или на темном фоне?",
        reply_markup=background_color_kb()
    )
    await bot.send_photo(chat_id=msg.chat.id,
                         photo="https://cloud.mail.ru/public/mPut/1pWyEikMm/светлый%20фон1.jpg",
                         caption="Светлый фон")
    await bot.send_photo(chat_id=msg.chat.id,
                         photo="https://cloud.mail.ru/public/mPut/1pWyEikMm/тёмный%20фон1.jpg",
                         caption="Тёмный фон")


@router.message(F.text.casefold().in_(["тёмный", "светлый"]), NewOrder.background)
async def go_dark_start(msg: types.Message, state: FSMContext):
    await state.update_data(background=msg.text)
    await state.set_state(NewOrder.phone)
    await msg.answer(
        "Оставьте ваш контактный номер, чтобы детально обсудить текущие моменты по съёмке вашей продукции."
    )


@router.message(NewOrder.name)
async def echo_message(msg: types.Message, bot: Bot, state: FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(NewOrder.type)
    await msg.answer(
        "Какого типа у вас съёмка? Каталожная (предметы на нейтральном фоне) или композиционная(творческая)?",
        reply_markup=type_photo_kb())
    await bot.send_photo(chat_id=msg.chat.id,
                         photo="https://cloud.mail.ru/public/mPut/1pWyEikMm/каталожная%2C%20нейтральный.jpg",
                         caption="Каталожная")
    await bot.send_photo(chat_id=msg.chat.id,
                         photo="https://cloud.mail.ru/public/mPut/1pWyEikMm/композиционна%2C%20творческая.jpg",
                         caption="Композиционная")
