from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji

artists = ['✡️ Оксимирон ✡️','🤡 Моргенштерн 🤡','🥷 Скриптонит 🥷']
artist = ReplyKeyboardMarkup(resize_keyboard=True)
for i in artists:
    artist.add(KeyboardButton(i))

# b1 = KeyboardButton('✡️ Оксимирон ✡️')
# b2 = KeyboardButton('🤡 Моргенштерн 🤡')
# b3 = KeyboardButton('🥷 Скриптонит 🥷')
b4 = KeyboardButton('🖋️ Вернуться к выбору поэта 🖋️')

# artist = ReplyKeyboardMarkup(resize_keyboard=True)
# artist.add(b1).add(b2).add(b3)

choice = ReplyKeyboardMarkup(resize_keyboard=True)
choice.add(b4)