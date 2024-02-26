import telebot
import random
from bot_token import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def choice_button(msg):
  keyboard = telebot.types.InlineKeyboardMarkup(row_width = 5)
  lst = []
  for i in range(5):
    lst.append(telebot.types.InlineKeyboardButton(text='❓', callback_data=str(i)))
  keyboard.row(*lst)
  bot.send_message(msg.chat.id, 'Нажми на кнопку:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def send_answer(call):
  num = random.randint(0, 4)
  if (call.data == str(num)):
    bot.send_message(call.message.chat.id, 'Ты выиграл!')
  else:
    bot.send_message(call.message.chat.id, 'Ты проиграл!')

  
if __name__ == '__main__':
  bot.polling(none_stop=True)