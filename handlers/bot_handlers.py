from aiogram import Dispatcher, types
from loader import dp
from keyboards import artist,choice
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from handlers import poem_generator


class Form(StatesGroup):
    artist = State()
    morgenshtern = State()
    oxxxymiron = State()
    skryptonite = State()
    morgenshtern_poem = State()
    oxxxymiron_poem = State()
    skryptonite_poem = State()
    result = State()

artists = ['✡️ Оксимирон ✡️','🤡 Моргенштерн 🤡','🥷 Скриптонит 🥷']

async def command_start(message : types.Message):
    await Form.artist.set()
    await message.answer('Выберите поэта 🎤', reply_markup = artist)

async def oxxxymiron(message : types.Message, state: FSMContext):
    await Form.oxxxymiron.set()
    await message.answer('Вы выбрали ✡️ Оксимирона ✡️\nНапишите первые строчки желаемого произведения:', reply_markup = ReplyKeyboardRemove())

async def morgenshtern(message : types.Message, state: FSMContext):
    await Form.morgenshtern.set()
    await message.answer('Вы выбрали 🤡 Моргенштерна 🤡\nНапишите первые строчки желаемого произведения:', reply_markup = ReplyKeyboardRemove())

async def skryptonite(message : types.Message, state: FSMContext):
    await Form.skryptonite.set()
    await message.answer('Вы выбрали 🥷 Скриптонита 🥷\nНапишите первые строчки желаемого произведения:', reply_markup = ReplyKeyboardRemove())

async def filter(message: types.Message, state: FSMContext):
    if message.text not in artists:
        await message.answer('Воспользуйся кнопками 💻️', reply_markup = artist)

async def oxxxymiron_generator(message : types.Message, state: FSMContext):
    text_message = poem_generator.gen_oxxxymiron(message.text)
    await Form.oxxxymiron.set()
    await message.answer(text_message, reply_markup=choice)

async def morgenshtern_generator(message : types.Message, state: FSMContext):
    text_message = poem_generator.gen_morgenshtern(message.text)
    await Form.morgenshtern.set()
    await message.answer(text_message, reply_markup = choice)

async def skryptonite_generator(message : types.Message, state: FSMContext):
    text_message = poem_generator.gen_scryptonite(message.text)
    await Form.skryptonite.set()
    await message.answer(text_message, reply_markup=choice)

async def set_default_commands():
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота")])

def register_bot_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands = ['start'], state='*')
    dp.register_message_handler(command_start, Text(equals="🖋️ Вернуться к выбору поэта 🖋️"), state='*')
    dp.register_message_handler(oxxxymiron, Text(equals="✡️ Оксимирон ✡️"), state=Form.artist)
    dp.register_message_handler(morgenshtern, Text(equals="🤡 Моргенштерн 🤡"), state=Form.artist)
    dp.register_message_handler(skryptonite, Text(equals="🥷 Скриптонит 🥷"), state=Form.artist)
    dp.register_message_handler(filter, state=Form.artist)
    dp.register_message_handler(oxxxymiron_generator, state=Form.oxxxymiron)
    dp.register_message_handler(morgenshtern_generator, state=Form.morgenshtern)
    dp.register_message_handler(skryptonite_generator, state=Form.skryptonite)
    dp.register_message_handler(set_default_commands)

