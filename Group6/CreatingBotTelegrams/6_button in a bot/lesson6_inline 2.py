import telebot
from bot_token import TOKEN
from random import choice

bot = telebot.TeleBot(TOKEN)

items = ['Камень 🗿', 'Ножницы ✂️', 'Бумага 📃']

msg_ids = {}

@bot.message_handler(commands=['game'])
def start_game(msg):
    keyboard = telebot.types.InlineKeyboardMarkup()
    for i in items:
        keyboard.add(telebot.types.InlineKeyboardButton(i, callback_data=i))
    bot_msg = bot.send_message(msg.chat.id, 'Что выберешь?', reply_markup=keyboard)
    msg_ids[msg.from_user.id] = bot_msg.message_id

@bot.callback_query_handler(func=lambda call: call.data in items)
def who_win(call):
    user_hod = call.data
    bot_hod = choice(items)
    text = f'Ты выбрал - {user_hod}\n'
    text += f'Я выбрал - {bot_hod}\n'
    if user_hod == bot_hod:
        text += 'Ничья'
    elif user_hod == 'Камень 🗿' and bot_hod == 'Ножницы ✂️' or \
         user_hod == 'Ножницы ✂️' and bot_hod == 'Бумага 📃' or \
         user_hod == 'Бумага 📃' and bot_hod == 'Камень 🗿':
        text += 'Ты победил'
    else:
        text += 'Я победил'
    bot.edit_message_text(text, call.message.chat.id, msg_ids[call.from_user.id])

@bot.callback_query_handler(func=lambda call: True)
def send_num(call):
    bot.send_message(call.message.chat.id, f'Нажата кнопка номер {call.data}')

# Пример расположения кнопок
@bot.message_handler(commands=['test'])
def test(msg):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Первая', callback_data='1'),
                 telebot.types.InlineKeyboardButton('Вторая', callback_data='2'))
    # работают ограничения
    keyboard.add(telebot.types.InlineKeyboardButton('Первая', callback_data='1'),
                 telebot.types.InlineKeyboardButton('Вторая', callback_data='2'),
                 telebot.types.InlineKeyboardButton('Третья', callback_data='3'),
                 telebot.types.InlineKeyboardButton('Четвертая', callback_data='4'))
    keyboard.row(telebot.types.InlineKeyboardButton('Первая', callback_data='1'),
                 telebot.types.InlineKeyboardButton('Вторая', callback_data='2'))
    # не работают ограничения
    keyboard.row(telebot.types.InlineKeyboardButton('Первая', callback_data='1'),
                 telebot.types.InlineKeyboardButton('Вторая', callback_data='2'),
                 telebot.types.InlineKeyboardButton('Третья', callback_data='3'),
                 telebot.types.InlineKeyboardButton('Четвертая', callback_data='4'))
    bot.send_message(msg.chat.id, 'Привет', reply_markup=keyboard)

if __name__ == '__main__':
    bot.infinity_polling()