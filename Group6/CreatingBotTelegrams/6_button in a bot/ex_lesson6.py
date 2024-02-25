import telebot
from bot_token import TOKEN

bot = telebot.TeleBot(TOKEN)

# создание клавиатуры
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
# добавление кнопок
keyboard.add('Кнопка 1', 'Кнопка 2', 'Кнопка 3', 'Кнопка 4', 'Кнопка 5', 'Кнопка 6', 'Кнопка 7', 'Кнопка 8')

@bot.message_handler(commands=['start'])
def send_key(msg):
    bot.send_message(msg.chat.id, 'Нажми кнопку', reply_markup=keyboard)

if __name__ == '__main__':
    bot.infinity_polling()
