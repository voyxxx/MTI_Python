import telebot
import requests
from bot_token import TOKEN 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['coffee'])
def get_coffee(msg):
  try:
   response = requests.get('https://coffee.alexflipnote.dev/random.json').json()
  except ConnectionError as e:
    print('Error', e)
  bot.send_photo(msg.chat.id, response['file'])

if __name__ == '__main__':
  bot.infinity_polling()