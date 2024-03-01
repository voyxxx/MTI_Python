import telebot
from bot_token import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_greeting(msg):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=12)
    markup.add(telebot.types.KeyboardButton('Text'))
    markup.add('Text')
    bot.send_message(msg.chat.id, 'Text', reply_markup=markup)

if __name__ == '__main__':
    bot.infinity_polling()