import telebot
from bot_token import TOKEN

bot = telebot.TeleBot(TOKEN)

pizzas = {
    'Маргарита': 500,
    'Пепперони': 600, 
    'Гавайская': 800,
    'Мясная': 100 
}

msgs_id = {}

carts = {}

def generate_keys_menu():
    keyboard = telebot.types.InlineKeyboardMarkup()
    for pizza in pizzas:
        keyboard.add(telebot.types.InlineKeyboardButton(f'{pizza} {pizzas[pizza]} руб.', callback_data=pizza))
    return keyboard

def generate_text_items(user_id):
    text = ''
    total = 0
    for pizza in carts[user_id]:
        text += f'{pizza} {pizzas[pizza]} руб.\n'
        total += pizzas[pizza]
    text += f'К оплате {total}'
    return text


@bot.message_handler(commands=['start'])
def send_greeting(msg):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Выбрать пиццу', callback_data='choice_pizza'))
    bot_msg = bot.send_message(msg.chat.id, 'Добро пожаловать в пиццерию "PIZZA". Хотите сделать заказ?', reply_markup=keyboard)
    msgs_id[msg.from_user.id] = bot_msg.message_id

@bot.callback_query_handler(func=lambda call: call.data == 'choice_pizza')
def choice_pizza(call):
    keyboard = generate_keys_menu()
    bot.edit_message_text('Выберите пиццу', call.message.chat.id, msgs_id[call.from_user.id], reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in pizzas)
def add_in_cart(call):
    if call.from_user.id in carts:
        carts[call.from_user.id].append(call.data)
    else:
        carts[call.from_user.id] = [call.data]
    text = generate_text_items(call.from_user.id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Добавить еще', callback_data='choice_pizza'))
    keyboard.add(telebot.types.InlineKeyboardButton('Оформить заказ', callback_data='place_order'))
    bot.edit_message_text(text, call.message.chat.id, msgs_id[call.from_user.id], reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'place_order')
def place_order(call):
    bot.send_message(call.message.chat.id, 'Ваш заказ оформлен. Ожидайте звонка администратора')

if __name__ == '__main__':
    bot.infinity_polling()