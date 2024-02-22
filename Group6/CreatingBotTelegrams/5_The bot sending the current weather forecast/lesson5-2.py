import telebot
from bot_token import TOKEN
from lesson5 import get_weather

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def get_location(msg):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(telebot.types.KeyboardButton('Поделиться местоположением', request_location=True))
    bot.send_message(msg.chat.id, 'Отправьте своё местоположение', reply_markup=keyboard)

@bot.message_handler(content_types=['location'])
def send_weather(msg):
    # print(msg)
    weather = get_weather(msg.location.latitude, msg.location.longitude)
    bot.send_message(msg.chat.id, weather, reply_markup=telebot.types.ReplyKeyboardRemove())

if __name__ == '__main__':
    bot.infinity_polling()