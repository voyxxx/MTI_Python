
import telebot
from bot_token import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'begin'])
def send_hello(message):
  bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')

@bot.message_handler(commands=['get_info'])
def get_info(message):
    bot.send_message(message.chat.id, f'{message.from_user.username} - {message.from_user.id}')

@bot.message_handler(func=lambda x: x.text.lower() in ['привет', 'здравствуй', 'добрый день'])
def greeting(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!😀👻')

@bot.message_handler(content_types=['sticker'])
def get_info_about_sticker(message):
    text = f"ID стикера - {message.sticker.file_id}, смайл - {message.sticker.emoji}"
    bot.send_message(chat_id=message.chat.id, text=text)
    
@bot.message_handler(content_types=['photo'])
def get_info_about_photo(message):
    print(message)
    bot.send_message(message.chat.id, f'ID фото - {message.photo[0].file_id}')

@bot.message_handler(content_types=['pinned_message'])
def get_info_about_pinned(message):
    print(message)
    bot.send_message(message.chat.id, f'{message.from_user.username} закрепил сообщение')

@bot.message_handler(content_types=['text'])
def echo(message):
    print(message)
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.infinity_polling()

