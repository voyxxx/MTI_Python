import telebot
from bot_token import TOKEN
from copy import deepcopy

bot = telebot.TeleBot(TOKEN)

locations = {
    '1': {
        'text': 'Ты оказываешься в густом и мрачном лесу, где каждый шаг может привести к опасностям. Деревья стоят плотной стеной, скрывая солнце и создавая полумрак. В воздухе висит густой туман, делая видимость минимальной.\nТвоя цель - найти выход из леса',
        'items': [],
        'next_move': {
            'К приключениям': '2'
        },
        'exchange': {}
    },
    '2': {
        'text': 'Ты попал на перекресток, впереди тебя три дороги.\nПервая дорога ведет к заброшенной хижине.\nВторая дорога ведет к болоту, полному опасных существ и ловушек.\nТретья дорога ведет к пещере\nКуда пойдешь?',
        'items': [],
        'next_move': {
            'Первая дорога': '3',
            'Вторая дорога': '4',
            'Третья дорога': '5'            
        },
        'exchange': {}
    },
    '3': {
        'text': 'Вы находитесь в глубоком лесу, где ветки склоняются к земле, создавая мрачное полотно над вашей головой. Вдалеке слышен шум потрескивающего костра и громкие голоса, напоминающие о чьей-то суете. По мере продвижения вперед, вы начинаете различать призрачные контуры заброшенного лагеря разбойников. Грубые хижины из дерева и кожи, окруженные колючей проволокой, выглядят опустошенными и забытыми. Только немного дыма поднимается из огня, а вокруг стоят вооруженные разбойники, собравшись вокруг костра, грозно бормоча и обсуждая свои коварные планы. Это конец...',
        'items': [],
        'next_move': {},
        'exchange': {}
    },
    '4': {
        'text': 'Вы попадаете на самую отдаленную и мистическую часть болота, где густой туман покрывает воду, словно покрывало. Среди зыбучих болотных топей вы замечаете маленькую островную гряду, на которой стоит старинная деревянная лодка, служащая мостом к торговцу. Торговец, облаченный в длинный плащ из засушенных листьев, улыбается вам, протирая пальцы, покрытые грязью. Его лавка уставлена разнообразными артефактами и тайными ингредиентами, извлеченными из самых глубинных уголков болота. Слухи ходят, что он обладает знанием о древних артефактах и способен обменять их на нечто более ценное.',
        'items': [],
        'next_move': {
            'Вернуться на перекресток': '2'
        },
        'exchange': {
            'шкатулка': 'золото: 3'
        }
    },
    '5': {
        'text': 'Вы оказываетесь перед огромным входом в темную и загадочную пещеру, из которой исходит холодный воздух, словно дыхание самой земли. Стены пещеры усыпаны мохом и лишайником, а потолок уходит в непостижимую тьму. При внимательном рассмотрении можно заметить странные рисунки и символы, вырезанные в камне, словно послание от давно забытой цивилизации.',
        'items': [],
        'next_move': {
            'Вернуться на перекресток': '2',
            'Осмотреться вокруг': '6',
            'Войти в пещеру': '7'
        },
        'exchange': {}
    },
    '6': {
        'text': 'В окрестностях пещеры царит дикая и грозная красота. Огромные скалы и утесы окружают вас, словно охраняя этот древний уголок от посторонних глаз. Скалы покрыты мхом и лишайником, а из щелей торчат корни деревьев, словно пытающиеся проникнуть внутрь, чтобы раскрыть тайны этого места. Ты побродил еще немного с целью что-то найти...',
        'items': ['шкатулка'],
        'next_move': {
            'Вернуться ко входу в пещеру': '5'
        },
        'exchange': {}
    },
    '7': {
        'text': 'Путешествуя вглубь пещеры, вы оказываетесь в сети извилистых ходов и темных проходов, словно лабиринт, сплетенный самой природой. Стены пещеры покрыты сталактитами и сталагтитами, создавая впечатление древнего святилища, утерянного во времени. Звук воды капающей с потолка создает пугающую атмосферу, напоминая о том, что вы не один в этих мрачных коридорах. За поворотом веднеется туннель. ',
        'items': ['золото: 2'],
        'next_move': {
            'Вернуться ко входу в пещеру': '5',
            'Пойти в туннель': '8'

        },
        'exchange': {}
    },
    '8': {
        'text': 'Вы заходите в узкий туннель, вырубленный в скале. Свет едва проникает сквозь узкие щели, создавая мрачные тени на стенах. Воздух в туннеле прохладный и влажный, а слабый шум капающей воды говорит о близости подземного потока. В конце туннеля вы видите свет',
        'items': [],
        'next_move': {
            'Вернуться назад': '7',
            'Идти дальше': '9'
        },
        'exchange': {}
    },
    '9': {
        'text': 'Вы находитесь в таинственной локации, окруженной мраком и загадками. Перед вами стоит проход, ведущий к выходу из этого места, но чтобы пройти, требуется заплатить пять золотых монет.',
        'items': [],
        'next_move': {
            'Вернуться назад': '8'
        },
        'exchange': {
            'золото: 5': 'выход'
        }
    }
}

users = {}

def generate_story(user_id):
    # название текущей локации
    current_location = users[user_id]['cur_pos']
    # получение текста текущей локации
    text = locations[current_location]['text']
    # генерация кнопок с дальнейшими хода
    keyboard = telebot.types.InlineKeyboardMarkup()
    for i in locations[current_location]['next_move']:
        keyboard.add(telebot.types.InlineKeyboardButton(i, callback_data=locations[current_location]['next_move'][i]))
    # идем циклом по списку предметов на локации
    for i in users[user_id]['loc'][current_location]['items']:
        # callback_data будет формата 'item предмет', например, 'item шкатулка'
        keyboard.add(telebot.types.InlineKeyboardButton(f'Взять предмет {i}', callback_data=f'item {i}'))
    # идем циклом по ключам словаря предметов для обмена на текущей локации
    for i in users[user_id]['loc'][current_location]['exchange']:
        if i in users[user_id]['items'] or i.startswith('золото: ') and users[user_id]['coins'] >= int(i.replace('золото: ', '')):
            text_key = f'Обменять предмет {i} на {users[user_id]["loc"][current_location]["exchange"][i]}'
            data_key = f'exchange {i}'
            keyboard.add(telebot.types.InlineKeyboardButton(text_key, callback_data=data_key))

    # добавление кнопок для запроса баланса или предметов, имеющихся у пользователя
    keyboard.add(
        telebot.types.InlineKeyboardButton('Баланс', callback_data='balance'),
        telebot.types.InlineKeyboardButton('Рюкзак', callback_data='backpack')
    )
    return text, keyboard

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, f'Привет! Если хочешь сыграть, то введи /game', reply_markup=telebot.types.ReplyKeyboardRemove())

@bot.message_handler(commands=['help'])
def help(msg):
    bot.send_message(msg.chat.id, 'Доступные команды:\n/game - начать игру')

@bot.message_handler(commands=['game'])
def start_game(msg):
    users[msg.from_user.id] = {'cur_pos': '1', 'coins': 0, 'items': [], 'loc': deepcopy(locations), 'msg_id': None}
    text, keyboard = generate_story(msg.from_user.id)
    msg_bot = bot.send_message(msg.chat.id, text, reply_markup=keyboard)
    users[msg.from_user.id]['msg_id'] = msg_bot.message_id


@bot.callback_query_handler(func=lambda call: call.data in locations)
def next_location(call):
    # меняем позицию игрока
    users[call.from_user.id]['cur_pos'] = call.data
    text, keyboard = generate_story(call.from_user.id)
    # вариант с отправкой новы сообщений
    # bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
    # вариант с редактированием сообщений
    bot.edit_message_text(text, call.message.chat.id, users[call.from_user.id]['msg_id'], reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('item '))
def get_item(call):
    # получаем название предмета
    item = call.data.replace('item ', '')
    # если название предмета начинается с 'золото: '
    if item.startswith('золото: '):
        # добавляем к балансу монет нужное кол-во монет
        users[call.from_user.id]['coins'] += int(item.replace('золото: ', ''))
    else:
        # добавляем предмет в список предметов пользователя 
        users[call.from_user.id]['items'].append(item)
    # берем название текущей локации пользователя
    current_location = users[call.from_user.id]['cur_pos']
    # удаляем предмет с текущей локации пользователя
    users[call.from_user.id]['loc'][current_location]['items'].remove(item)
    text, keyboard = generate_story(call.from_user.id)
    bot.edit_message_text(text, call.message.chat.id, users[call.from_user.id]['msg_id'], reply_markup=keyboard)
    # показываем уведомление о взятии предмета
    bot.answer_callback_query(call.id, f'Вы взяли предмет {item}')

@bot.callback_query_handler(func=lambda call: call.data.startswith('exchange '))
def change_items(call):
    # берем название текущей локации пользователя
    current_location = users[call.from_user.id]['cur_pos']
    # получаем название предмета (который отдает пользователь)
    item_1 = call.data.replace('exchange ', '')
    # получаем название предмета (который получает взамен пользователь)
    item_2 = users[call.from_user.id]['loc'][current_location]['exchange'][item_1]
    # если название предмета начинается с 'золото: '
    if item_1.startswith('золото: '):
        # отнимаем от баланса монет нужное кол-во монет
        users[call.from_user.id]['coins'] -= int(item_1.replace('золото: ', ''))
    else:
        # удалем предмет из списка предметов пользователя 
        users[call.from_user.id]['items'].remove(item_1)
    
    # если название предмета начинается с 'золото: '
    if item_2.startswith('золото: '):
        # добавляем к балансу монет нужное кол-во монет
        users[call.from_user.id]['coins'] += int(item_2.replace('золото: ', ''))
    else:
        # добавляем предмет в список предметов пользователя 
        users[call.from_user.id]['items'].append(item_2)

    # удаляем обмен с локации
    users[call.from_user.id]['loc'][current_location]['exchange'].pop(item_1)

    if item_2 == 'выход':
        bot.edit_message_text('Ура! Ты выиграл!!!', call.message.chat.id, users[call.from_user.id]['msg_id'])
    else:
        text, keyboard = generate_story(call.from_user.id)
        bot.edit_message_text(text, call.message.chat.id, users[call.from_user.id]['msg_id'], reply_markup=keyboard)
        # показываем уведомление об обмене
        bot.answer_callback_query(call.id, f'Вы обменяли предмет {item_1} на {item_2}')


@bot.callback_query_handler(func=lambda call: call.data == 'balance' and call.message.id == users[call.from_user.id]['msg_id']) 
def show_balance(call):
    # выводим в уведомлении баланс пользователя
    bot.answer_callback_query(call.id, f'Ваш баланс: {users[call.from_user.id]["coins"]} монет', show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data == 'backpack')
def show_items(call):
    # если у пользователя есть предметы
    if users[call.from_user.id]['items']:
        # выводим в уведомлении список предметов пользователя
        bot.answer_callback_query(call.id, 'Ваши предметы: ' + ', '.join(users[call.from_user.id]['items']), show_alert=True)
    else:
        # вводим в уведомлении, что нет предметов
        bot.answer_callback_query(call.id, 'У вас нет предметов', show_alert=True)

if __name__ == '__main__':
    bot.infinity_polling()