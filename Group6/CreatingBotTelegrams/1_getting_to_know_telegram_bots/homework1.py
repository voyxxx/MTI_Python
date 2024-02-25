import telebot
from bot_token import TOKEN 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def echoTenthPower(message):
  print(message)
  print('message.text', message.text)
  bot.send_message(message.chat.id, message.text * 10)

if __name__ == '__main__':
    bot.infinity_polling()
    