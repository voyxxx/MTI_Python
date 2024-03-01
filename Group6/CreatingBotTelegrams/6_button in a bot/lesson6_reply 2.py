import telebot
from bot_token import TOKEN
from random import choice

bot = telebot.TeleBot(TOKEN)

jokes = [
    'У меня была одна проблема, поэтому я решил написать программу, которая её решит. Теперь у меня есть 1 проблема, 9 ошибок и 12 предупреждений.',
    'Если бы программисты были врачами, им бы говорили «У меня болит нога», а они отвечали «Ну не знаю, у меня такая же нога, а ничего не болит»',
    'Хороший программист проливает кофе на себя. И ноут цел, и бодрит в два раза лучше.'
]

@bot.message_handler(commands=['start'])
def send_keyboard(msg):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Случайный анекдот')
    bot.send_message(msg.chat.id, 'Привет! Я умею отправлять анекдоты', reply_markup=keyboard)

@bot.message_handler(func=lambda msg: msg.text == 'Случайный анекдот')
def send_joke(msg):
    bot.send_message(msg.chat.id, choice(jokes))

@bot.message_handler(commands=['test'])
def test(msg):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Первая', 'Вторая')
    keyboard.add('Первая', 'Вторая', 'Третья', 'Четвертая')
    keyboard.row('Первая', 'Вторая')
    keyboard.row('Первая', 'Вторая', 'Третья', 'Четвертая')
    bot.send_message(msg.chat.id, 'Привет', reply_markup=keyboard)

if __name__ == '__main__':
    bot.infinity_polling()