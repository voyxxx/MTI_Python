import telebot
import random
from bot_token import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def findRandomWord(message):
  if 'рандом' in message.text:
    bot.send_message(message.chat.id, f'Случайное число:{str(random.randint(0, 100))}')
  else:
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
  bot.infinity_polling()