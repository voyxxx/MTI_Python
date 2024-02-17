import telebot
from bot_token import TOKEN
import requests

bot = telebot.TeleBot(TOKEN)
# path = 'Group6\\CreatingBotTelegrams\\3_Working with the file system\\'


@bot.message_handler(commands=['cat'])
def send_cat(message):
    response = requests.get('https://cataas.com/cat?json=true').json()
    url = f"https://cataas.com/cat/{response['_id']}"
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands=['cat_with_text'])
def send_question(msg):
    msg_2 = bot.send_message(msg.chat.id, 'Введите текст')
    bot.register_next_step_handler(msg_2, send_cat_with_text)

def send_cat_with_text(msg):
    r = requests.get('https://cataas.com/cat?json=true').json()
    url = f"https://cataas.com/cat/{r['_id']}/says/{msg.text}"
    bot.send_photo(msg.chat.id, url)

if __name__ == '__main__':
  bot.infinity_polling()

""" 
https://randomfox.ca/floof/
https://random-d.uk/api
https://random.dog/woof.json

https://demo.deeppavlov.ai/#/examples/odqa
"""