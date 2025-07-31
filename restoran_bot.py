import asyncio
import logging
import sys
from math import lgamma
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, BotCommand, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()

TOKEN =  "8282576791:AAFPzNp0uWkWcNGR43AiMAooGKInBRG_-BE"

dp = Dispatcher()


def make_reply_btn(btns, sizes):
    rkb = ReplyKeyboardBuilder()
    rkb.add(*btns)
    rkb.adjust(*sizes)
    return rkb.as_markup(resize_keyboard=True)


class StepByStepState(StatesGroup):
    menu = State()
    btn1 = State()
    btn1_2 = State()


@dp.message(StepByStepState.btn1, F.func(lambda message: message.text == "back"))
@dp.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    btns = [
        KeyboardButton(text="🍽 Restoran menyusi"),
        KeyboardButton(text="☎️ Biz bilan bog'lanish")
    ]
    markup = make_reply_btn(btns, [2])
    await state.set_state(StepByStepState.menu)
    await message.answer("Choice: ", reply_markup=markup)


@dp.message(StepByStepState.btn1_2, F.func(lambda message: message.text == "back Asosiy menuga qaytish"))
@dp.message(StepByStepState.menu, F.func(lambda message: message.text == "🍽 Restoran menyusi"))
async def start_handler(message: Message, state: FSMContext):
    btns = [
        KeyboardButton(text="🥗 Salatlar"),
        KeyboardButton(text="🍟 Fast food"),
        KeyboardButton(text="🍵 issiq taomlar"),
        KeyboardButton(text="back Asosiy menuga qaytish")
    ]
    markup = make_reply_btn(btns, [3,1])
    await state.set_state(StepByStepState.btn1)
    await message.answer("Menyudan tanlang :  ", reply_markup=markup)


@dp.message(StepByStepState.btn1, F.func(lambda message: message.text == "🥗 Salatlar"))
async def start_handler(message: Message, state: FSMContext):
    btns = [
        KeyboardButton(text="🥗 Sezar salati"),
        KeyboardButton(text="🥗 Olivye salati"),
        KeyboardButton(text="back Asosiy menuga qaytish")
    ]
    markup = make_reply_btn(btns, [2, 1])
    await state.set_state(StepByStepState.btn1_2)
    await message.answer("Choice: ", reply_markup=markup)




@dp.message(StepByStepState.btn1, F.func(lambda message: message.text == "🍟 Fast food"))
async def start_handler(message: Message, state: FSMContext):
    btns = [
        KeyboardButton(text="🍔 Burger"),
        KeyboardButton(text=" 🌭 Hot-dog"),
        KeyboardButton(text="back Asosiy menuga qaytish")
    ]
    markup = make_reply_btn(btns, [2, 1])
    await state.set_state(StepByStepState.btn1_2)
    await message.answer("Choice: ", reply_markup=markup)



@dp.message(StepByStepState.btn1, F.func(lambda message: message.text == "🍵 issiq taomlar"))
async def start_handler(message: Message, state: FSMContext):
    btns = [
        KeyboardButton(text="🥘 Osh"),
        KeyboardButton(text="🍵 Shurva"),
        KeyboardButton(text="back Asosiy menuga qaytish")
    ]
    markup = make_reply_btn(btns, [2, 1])
    await state.set_state(StepByStepState.btn1_2)
    await message.answer("Choice: ", reply_markup=markup)





@dp.message(StepByStepState.btn1_2, F.func(lambda message: message.text == "back"))
@dp.message(StepByStepState.menu, F.func(lambda message: message.text == "☎️ Biz bilan bog'lanish"))
async def start_handler(message: Message, state: FSMContext):
    btns = [
        KeyboardButton(text="Contact ☎️", request_contact=True),
    ]
    markup = make_reply_btn(btns, [1])
    await state.set_state(StepByStepState.btn1)
    await message.answer("Choice: ", reply_markup=markup)







# @dp.message(StepByStepState.btn1, F.func(lambda message: message.text == "Qarshi"))
# async def start_handler(message: Message, state: FSMContext):
#     btns = [
#         KeyboardButton(text="Reject"),
#         KeyboardButton(text="Accept"),
#         KeyboardButton(text="back")
#     ]
#     markup = make_reply_btn(btns, [2,2, 1])
#     await state.set_state(StepByStepState.btn1_2)
#     await message.answer("Choice: ", reply_markup=markup)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
