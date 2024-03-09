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
        'exchange': {}
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
        'items': [],
        'next_move': {
            'Вернуться ко входу в пещеру': '5'
        },
        'exchange': {}
    },
    '7': {
        'text': 'Путешествуя вглубь пещеры, вы оказываетесь в сети извилистых ходов и темных проходов, словно лабиринт, сплетенный самой природой. Стены пещеры покрыты сталактитами и сталагтитами, создавая впечатление древнего святилища, утерянного во времени. Звук воды капающей с потолка создает пугающую атмосферу, напоминая о том, что вы не один в этих мрачных коридорах. За поворотом веднеется туннель. ',
        'items': [],
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
        'exchange': {}
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
    return text, keyboard

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


if __name__ == '__main__':
    bot.infinity_polling()