import telebot
from bot_token_first import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_key(msg):
    keyboard = telebot.types.InlineKeyboardMarkup()
    for i in range(1, 6):
        keyboard.add(telebot.types.InlineKeyboardButton(text=str(i), callback_data=str(i)))
    bot.send_message(msg.chat.id, 'Нажми на кнопку:', reply_markup=keyboard)

@bot.message_handler(commands=['start2'])
def send_key_2(msg):
    keyboard = telebot.types.InlineKeyboardMarkup()
    lst = []
    for i in range(1, 6):
        lst.append(telebot.types.InlineKeyboardButton(text='❄', callback_data=str(i)))
    keyboard.add(*lst)
    keyboard.row(*lst)
    bot.send_message(msg.chat.id, 'Нажми на кнопку:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def send_answer(call):
    bot.send_message(call.message.chat.id, f'Ты выбрал {call.data} кнопку')

if __name__ == '__main__':
    bot.infinity_polling()