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
def send_greeting(msg):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Случайный анекдот')
    bot.send_message(msg.chat.id, 'Привет! Нажми кнопку и я отправлю анекдот', 
                     reply_markup=keyboard)
    
@bot.message_handler(func=lambda x: x.text == 'Случайный анекдот')
def send_joke(msg):
    bot.send_message(msg.chat.id, choice(jokes))

#  ПРИМЕРЫ РАСПОЛОЖЕНИЙ
@bot.message_handler(commands=['start2'])
def send_greeting_2(msg):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    lst = []
    for i in range(1, 6):
        lst.append(f'Кнопка {i}')
    keyboard.add(*lst)
    keyboard.add('Кнопка 10')
    keyboard.row(*lst)
    bot.send_message(msg.chat.id, 'Привет! Нажми кнопку и я отправлю анекдот', 
                     reply_markup=keyboard)

if __name__ == '__main__':
    bot.infinity_polling()