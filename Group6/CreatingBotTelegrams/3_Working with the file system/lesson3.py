import telebot
from bot_token import TOKEN
from gtts import gTTS

bot = telebot.TeleBot(TOKEN)
path = 'Group6/CreatingBotTelegrams/3_Working with the file system/'
@bot.message_handler(commands=['photo'])
def photo(message):
  try :
    # photo = open('/Users/VB/Pictures/iphone13_01:01:24/IMG_1128.HEIC', 'rb')
    photo = open('Group6/CreatingBotTelegrams/3_Working with the file system/IMG_1128.HEIC', 'rb')
    bot.send_photo(message.chat.id, photo)
  except FileNotFoundError:
    bot.send_message(message.chat.id, 'Фото не найдено')
  bot.send_photo(message.chat.id, 'https://aif-s3.aif.ru/images/026/400/fa1add6839ae97c9a27a7d0cd160cc9f.jpg')

@bot.message_handler(commands=['audio'])
def audio(message):
  audioFile = ('/', 'rb')
  bot.send_audio(message.chat.id, 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')

@bot.message_handler(commands=['doc'])
def doc(message):
  docFile = ('/', 'rb')
  bot.send_document(message.chat.id, docFile)

@bot.message_handler(commands=['gif'])
def gif(message):
  # gifFile = ('/', 'rb')
  # bot.send_animation(message.chat.id, gifFile)
  bot.send_animation(message.chat.id, 'https://tenor.com/RqVy.gif')

@bot.message_handler(commands=['text'])
def send_speech(message):
  speech  = gTTS(message.text, lang='ru')
  speech.save(f'media/{message.chat.id}_{message.id}_voice.ogg')
  bot.send_voice(message.chat.id, open(f'media/{message.chat.id}_{message.id}_voice.ogg', 'rb'))

if __name__ == '__main__':
  bot.infinity_polling()
