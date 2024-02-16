import telebot
from bot_token import TOKEN
from gtts import gTTS
from random import choice

bot = telebot.TeleBot(TOKEN)
path = 'Group6\\CreatingBotTelegrams\\3_Working with the file system\\'


@bot.message_handler(commands=['photo'])
def photo(message):
  try :
    # photo = open('/Users/VB/Pictures/iphone13_01:01:24/IMG_1128.HEIC', 'rb')
    photo = open('./media/IMG_1128.HEIC', 'rb')
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
  docFile = ('/task.txt', 'rb')
  bot.send_document(message.chat.id, docFile)

@bot.message_handler(commands=['gif'])
def gif(message):
  bot.send_animation(message.chat.id, 'https://media1.tenor.com/m/WmIEqvGZKxsAAAAC/lol.gif')

@bot.message_handler(commands=['group'])
def group(message):
    imgs = [
        telebot.types.InputMediaPhoto('https://famt.ru/wp-content/uploads/2019/05/sonnik-govoryaschiy-kot.jpg'),
        telebot.types.InputMediaPhoto('https://famt.ru/wp-content/uploads/2019/05/sonnik-govoryaschiy-kot.jpg')
    ]
    bot.send_media_group(message.chat.id, imgs)

@bot.message_handler(commands=['venue'])
def venue(message):
    bot.send_venue(message.chat.id, 47, 45, 'Название места', 'адрес')

@bot.message_handler(commands=['poll'])
def poll(message):
    bot.send_poll(message.chat.id, 'Как дела?', ['ок', 'не ок'], False)

@bot.message_handler(commands=['dice'])
def dice(message):
    bot.send_dice(message.chat.id, '🎲')
    bot.send_dice(message.chat.id, '🎯')
    bot.send_dice(message.chat.id, '🏀')
    bot.send_dice(message.chat.id, '⚽')
    bot.send_dice(message.chat.id, '🎳')
    bot.send_dice(message.chat.id, '🎰')

@bot.message_handler(content_types=['sticker'])
def sticker(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)    

@bot.message_handler(content_types=['video'])
def video(message):
    # получаем id файла
    video_id = message.video.file_id
    # получаем путь
    video_path = bot.get_file(video_id).file_path
    # скачиваем файл
    video = bot.download_file(video_path)
    bot.send_video_note(message.chat.id, video)


@bot.message_handler(content_types=['text'])
def send_speech(message):
    speech = gTTS(message.text, lang='ru')
    speech.save(f'media/{message.chat.id}_{message.id}.ogg')
    bot.send_voice(message.chat.id, open(f'media/{message.chat.id}_{message.id}.ogg', 'rb'))
    lst = ['🤞','✌️','👍','😁','💕','😘','😂','🤣','❤️','😍','🎶','😎','😉']
    bot.set_message_reaction(message.chat.id, message.id, [telebot.types.ReactionTypeEmoji(choice(lst))])

if __name__ == '__main__':
  bot.infinity_polling()


# Комментарии: Чтобы video note отправлялся именно в кружке нужно соблюдать следующие условия:
# Бот должен отправлять кружок не по id файла, а сначала скачивать его, а потом для отправки использовать сохраненное видео
# Когда будете тестировать, необходимо отправлять квадратное видео в самом плохом качестве (как это сделать - https://drive.google.com/file/d/1RtmKfR7FejE3xCJF7yfQvj0_5Jn2E1Pd/view?usp=drive_link )