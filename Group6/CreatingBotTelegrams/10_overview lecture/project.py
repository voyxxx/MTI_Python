import random
import telebot
from bot_token import TOKEN
from copy import deepcopy

bot = telebot.TeleBot(TOKEN)

planets = {
    '1': {
        'text': 'Призрачные Спектры - это эфирные существа, живущие планете **Туманность**, полной газов и пыли. Основной ресурс - редкий газ, используемые для межзвездных путешествий. Их неспособность физически защищать свои ресурсы делает их уязвимыми для краж. Слабость: Незаметно украсть.',
        'species': 'призрачные спектры',
        'planet': 'туманность',
        'resource': 'редкий газ',
        'weakness': ['steal'],
    },
    '2': {
        'text': 'Бронированные Титаны - это мощные существа, обитающие на планете-гиганте **Титан-7**, покрытой мощной броней. Основной ресурс - металлы и минералы, используемые для производства оружия и брони. Их жадность и склонность к роскоши делает их уязвимыми для покупки. Слабость: Купить.',
        'species': 'бронированные титаны',
        'planet': 'титан-7',
        'resource': 'металлы и минералы',
        'weakness': ['buy'],
    },
    '3': {
        'text': 'Мирные Зеффиры - это существа, живущие в гармонии с природой на планете Зефир-9 с сильными ветрами. Основной ресурс - энергия ветра, используемая для выработки электроэнергии. Их неспособность защитить свои ресурсы от силового захвата делает их уязвимыми для отобрать силой. Слабость: Отобрать силой.',
        'species': 'мирные зеффиры',
        'planet': 'зефир-9',
        'resource': 'энергия ветра',
        'weakness': ['takeByForce'],
    },
    '4': {
        'text': 'Хитроумные Трикстеры - это умные и коварные существа, населяющие планету-лабиринт Триксис. Основной ресурс - редкие кристаллы, используемые для создания передовых технологий. Их ресурсы можно легко украсть, если вы хитрее их. Слабость: Незаметно украсть.',
        'species': 'хитроумные трикстеры',
        'planet': 'триксис',
        'resource': 'редкие кристаллы',
        'weakness': ['steal'],
    },
    '5': {
        'text': 'Богатые Плутократы - это богатые и могущественные существа, контролирующие богатую планету Плутократия. Основной ресурс - драгоценные металлы и камни, используемые для создания ювелирных изделий и денег. Их жадность делает их уязвимыми для краж и покупок. Слабость: Незаметно украсть, Купить.',
        'species': 'богатые плутократы',
        'planet': 'плутократия',
        'resource': 'драгоценные металлы и камни',
        'weakness': ['steal']
    },
    '6': {
        'text': 'Воинственные Берсеркеры - это агрессивные существа, населяющие планету-вулкан Берсерк. Основной ресурс - огонь и лава, используемые для производства оружия и энергии. Их агрессивность и неспособность контролировать свои эмоции делает их уязвимыми для обмана и краж. Слабость: Незаметно украсть, Отобрать силой.',
        'species': 'воинственные берсеркеры',
        'planet': 'берсерк',
        'resource': 'огонь и лава',
        'weakness': ['steal', 'takeByForce']
    },
    '7': {
        'text': 'Землекопы Гномы - это трудолюбивые существа, живущие на подземной планете Гномония. Основной ресурс - драгоценные металлы и камни, добываемые в подземных шахтах. Их ресурсы легко можно купить, но их подземные туннели делают их уязвимыми для краж. Слабость: Незаметно украсть, Купить.',
        'species': 'землекопы гномы',
        'planet': 'гномония',
        'resource': 'драгоценные металлы и камни',
        'weakness': ['steal', 'buy']
    },
    '8': {
        'text': 'Знатоки Прометея - это высокоразвитые существа, населяющие планету Прометей. Основной ресурс Прометея - это технологии и инновации. Эти существа обладают невероятной способностью к изобретениям и созданию передовых технологий. Планета Прометей покрыта футуристическими городами и лабораториями, где Знатоки неустанно работают над созданием новых изобретений. Они постоянно стремятся к совершенству и не останавливаются перед ничтожными препятствиями. Однако, их поглощенность работой и изобретениями делает их уязвимыми для внешних атак. Они не имеют сильной армии или защитных систем. Слабость: Отобрать силой, незаметно украсть.',
        'species': 'знатоки прометея',
        'planet': 'прометей',
        'resource': 'технологии и инновации',
        'weakness': ['steal', 'takeByForce']
    },
    '9': {
        'text': 'Золотой Рай - это необитаемая планета, покрытая золотыми песками. Основной ресурс - золото, которое может быть использовано для создания ювелирных изделий и денег.',
        'species': '',
        'planet': 'золотой рай',
        'resource': 'золото',
        'weakness': [],
    },
    '10': {
        'text': 'Ледяная Твердыня - это необитаемая планета, покрытая льдом и снегом. Основной ресурс - вода, которая может быть использована для выращивания растений и поддержания жизни.',
        'species': '',
        'planet': 'ледяная твердыня',
        'resource': 'вода',
        'weakness': [],
    },
    '11': {
        'text': 'После многих лет путешествий, мы, наконец, достигли планеты Сапиенция, населенной мудрыми и всезнающими существами. Эта планета, покрытая огромными библиотеками, является источником мудрости и знаний во всей галактике. Жители Сапиенции, известные как Сапиенты, обладают невероятной способностью к обучению и пониманию всего вокруг них. Основной ресурс Сапиенции - это знания и информация, хранящиеся в библиотеках. Мы рады, что наконец-то достигли этой планеты, и не можем дождаться, чтобы начать наше обучение с Сапиентами. Это действительно чудесное место, и мы знаем, что мы вернемся домой с несметным количеством знаний и мудрости.',
        'species': 'сапиенты',
        'planet': 'cапиенция',
        'resource': '',
        'weakness': [],
    },
}

questions = {
    '1': lambda _: f'С какой планеты вы прибыли?',
    '2': lambda planet: f'Какой основной ресурс на планете {planet}?',
    '3': lambda specie: f'На какой планете обитает раса {specie}?',
    '4': lambda _: f'Название вашей родной планеты?',
}

greeting = 'Вы готовы отправиться в путешествие к самой мудрой и всезнающей цивилизации во вселенной? Планета, населенная существами, которые собрали все знания и информацию во вселенной в огромные библиотеки, ожидает вас. Вы сможете обучаться у этих мудрых существ и получить доступ к несметным знаниям и мудрости.\nВаша цель добраться до планеты cапиенция.'

locations = {
    '1': {
        'text': '',
        'isVisited': 'false',
        'distances': {
            '2': 3,
            '3': 3,
            '4': 6,
            '5': 6,
            '6': 9,
            '7': 9,
            '8': 12,
            '9': 15,
            '10': 6,
            '11': 16
        },
    },
    '2': {
        'text': '',
        'isVisited': 'false',
        'distances': {
            '1': 3,
            '3': 6,
            '4': 3,
            '5': 9,
            '6': 6,
            '7': 12,
            '8': 9,
            '9': 12,
            '10': 6,
            '11': 16
        },
    },
    '3': {
        'text': '',
        'isVisited': 'false',
        'distances': {
            '1': 3,
            '2': 6,
            '4': 9,
            '5': 3,
            '6': 12,
            '7': 6,
            '8': 9,
            '9': 12,
            '10': 6,
            '11': 16
        },
    },
    '4': {
        'text': '',
        'isVisited': 'false',
        'distances': {
            '1': 6,
            '2': 3,
            '3': 9,
            '5': 12,
            '6': 3,
            '7': 9,
            '8': 6,
            '9': 9,
            '10': 9,
            '11': 19
        },
    },
    '5': {
        'text': '',
        'isVisited': 'false',
        'distances': {
            '1': 6,
            '2': 9,
            '3': 3,
            '4': 12,
            '6': 9,
            '7': 3,
            '8': 6,
            '9': 9,
            '10': 9,
            '11': 19
        },
    },
    '6': {
        'text': '',
        'isVisited': 'false',
        'distances': {
            '1': 9,
            '2': 6,
            '3': 12,
            '4': 3,
            '5': 9,
            '7': 6,
            '8': 3,
            '9': 6,
            '10': 12,
            '11': 16
        },
    },
    '7': {
        'text': '',
        'isVisited': 'false',
        'distances': {
            '1': 9,
            '2': 12,
            '3': 6,
            '4': 9,
            '5': 3,
            '6': 6,
            '8': 3,
            '9': 6,
            '10': 12,
            '11': 16
        },
    },
    '8': {
        'text': '',
        'isVisited': 'false',
        'distances': {
            '1': 12,
            '2': 9,
            '3': 9,
            '4': 6,
            '5': 6,
            '6': 3,
            '7': 3,
            '9': 6,
            '10': 15,
            '11': 16
        },
    },
    '9': {
        'text': '',
        'isVisited': 'false',
        'distances': {
            '1': 15,
            '2': 12,
            '3': 12,
            '4': 9,
            '5': 9,
            '6': 6,
            '7': 6,
            '8': 6,
            '10': 18,
            '11': 10
        },
    },
    '10': {
        'text': '',
        'isVisited': 'false',
        'distances': {
            '1': 6,
            '2': 6,
            '3': 6,
            '4': 9,
            '5': 9,
            '6': 12,
            '7': 12,
            '8': 15,
            '9': 18,
            '11': 10
        },
    },
    '11': {
        'text': '',
        'isVisited': 'false',
        'distances': {
            '1': 16,
            '2': 16,
            '3': 16,
            '4': 19,
            '5': 19,
            '6': 16,
            '7': 16,
            '8': 16,
            '9': 10,
            '10': 10
        }
    }
}

actions = {
    'move': 'Отправиться на другую планету.',
    'answer': 'Ответить на вопрос.',
    'risk': 'Рискнуть своей жизнью. Выигрыш 500 монет.',
    'buy': 'Купить топливо.',
    'steal': 'Украсть топливо.',
    'takeByForce': 'Отобрать топливо силой.',
}

game_locations = {}

players = {
    'player1': {
        'name': 'мощь',
        'power': 5,
        'agility': 0,
        'eloquence': 0
    },
    'player2': {
        'name': 'проворность',
        'power': 0,
        'agility': 5,
        'eloquence': 0
    },
    'player3': {
        'name': 'убедительность',
        'power': 0,
        'agility': 0,
        'eloquence': 5
    }
}

player = {}


def endGame(chatId):
    global player
    player[chatId]['gameIsBegin'] = False


def getCurGoldAndFuel(userId):
    global player
    return f'доступно кол-во топлива: {player[userId]["fuel"]}, кол-во золота {player[userId]["gold"]}'


# Обработка нажатия кнопки назад
@bot.callback_query_handler(func=lambda call: call.data == 'back')
def handlerBack(call):
    chatId = call.message.chat.id
    userId = call.from_user.id
    startTrip(chatId, userId)


# Ловим событие нажатия кнопки с планетой (перемещение на планету)
@bot.callback_query_handler(func=lambda call: call.data.startswith('planet'))
def moveToPlanet(call):
    global player
    chatId = call.message.chat.id
    userId = call.from_user.id
    currentPlanetNum = call.data.removeprefix('planet')

    # Получить текущую планету и текущее количество топлива
    previousPlanetNumber = player[userId]['currentPlanetNumber']
    player[userId]['previousPlace'] = player[userId]['loc'][str(previousPlanetNumber)]
    player[userId]['currentPlanetNumber'] = currentPlanetNum

    # Получить затраты топлива до выбранной планеты
    spentFuel = player[userId]['loc'][str(previousPlanetNumber)]['distances'][str(currentPlanetNum)]
    # Обновляем кол-во топлива
    player[userId]['fuel'] -= spentFuel
    # Обновляем номер текущей планеты
    player[userId]['currentPlanetNumber'] = currentPlanetNum
    # Помечаем, что текущая планета посещена
    player[userId]['loc'][str(currentPlanetNum)]['isVisited'] = True

    # Проверить, является ли выбранная планета целевой
    if player[userId]['loc'][str(currentPlanetNum)]['planet'] == 'cапиенция':
        text = ('Поздравляем! Вы достигли целевой планеты и победили в игре!\nЧтобы сыграть ещё раз введите команду '
                '/game')
        bot.edit_message_text(text, chatId, player[userId]['msgId'])
        endGame(userId)
        return

    fuelPenalty = player[userId]['fuelPenalty']
    # Проверить, является ли выбранная планета пустой и нет ли топлива
    lenSpecies = len(player[userId]['loc'][currentPlanetNum]['species'])
    if (len(player[userId]['loc'][currentPlanetNum]['species']) == 0) and (player[userId]['fuel'] < (6 + fuelPenalty)):
        text = ('Вы оказались на пустой планете. У вас не хватает топлива на очередной перелёт, поэтому вы проиграли '
                'игру.\nПопробуйте сыграть ещё раз. Для этого введите команду /game')
        bot.edit_message_text(text, chatId, player[userId]['msgId'])
        endGame(userId)
        return

    startTrip(chatId, userId)


# Посмотреть список доступных для путешествия планет
def checkAllowedPlanet(userId):
    global player
    currentPlanetDistances = player[userId]['loc'][str(player[userId]['currentPlanetNumber'])]['distances']
    fuel = player[userId]['fuel']
    fuelPenalty = player[userId]['fuelPenalty']
    player[userId]['allowedDistances'] = {}
    for distance in currentPlanetDistances:
        if currentPlanetDistances[distance] + fuelPenalty <= fuel:
            player[userId]['allowedDistances'].update({distance: currentPlanetDistances[distance]})


# Отобразить список доступных для путешествия планет
def displayMoveVariants(chatId, userId):
    keyboard = telebot.types.InlineKeyboardMarkup()
    text = ''
    if len(player[userId]['allowedDistances']) >= 0:
        for planetNum in player[userId]['allowedDistances']:
            planet = player[userId]['loc'][planetNum]['planet']
            keyboard.add(
                telebot.types.InlineKeyboardButton(
                    f'{planet} - {player[userId]["allowedDistances"][planetNum]} топлива',
                    callback_data=f'planet{planetNum}'))
        text = f'Сейчас {getCurGoldAndFuel(userId)}. Вам доступны путешествия на следующие планеты:'
    else:
        text = f'Доступных планет нет, {getCurGoldAndFuel(userId)}.'
    keyboard.add(telebot.types.InlineKeyboardButton('вернуться назад', callback_data='back'))
    bot.edit_message_text(text, chatId, player[userId]['msgId'], reply_markup=keyboard)


# Обработка нажатия кнопки назад
@bot.callback_query_handler(func=lambda call: call.data.startswith('question'))
def handlerAskQuestion(call):
    chatId = call.message.chat.id
    userId = call.from_user.id
    _, isRight, questionNum = call.data.split(',')
    if isRight == 'True':
        gold = 2 if questionNum == 4 else 3 if questionNum == 1 else 5
        player[userId]['gold'] += gold
        text = f'Ответ верный. Вы заработали {gold} золота'
    else:
        text = 'Ответ не верный'
    bot.answer_callback_query(call.id, text, show_alert=True)
    startTrip(chatId, userId)


def askQuestion(chatId, userId):
    questionNum = int(random.randint(1, 4))
    questionNum = 2
    if questionNum == 1 and 'previousPlace' not in player[userId]:
        questionNum = str(random.randint(2, 4))
    currentPlanet = player[userId]['loc'][str(player[userId]['currentPlanetNumber'])]
    randomPlanet = player[userId]['loc'][str(random.randint(1, 9))]
    correctAnswer = ''
    while randomPlanet['planet'] == currentPlanet['planet']:
        randomPlanet = player[userId]['loc'][str(random.randint(1, 9))]
    keyboard = telebot.types.InlineKeyboardMarkup()
    if questionNum == 1 or questionNum == 3 or questionNum == 4:
        planet_names = [planet['planet'] for planet in player[userId]['loc'].values()]
        if questionNum == 1:
            correctAnswer = player[userId]['previousPlace']['planet']
        elif questionNum == 3:
            correctAnswer = randomPlanet['planet']
        elif questionNum == 4:
            correctAnswer = player[userId]['birthPlace']['planet']
        for planet_name in planet_names:
            data = f'question,{planet_name == correctAnswer}'
            keyboard.add(
                telebot.types.InlineKeyboardButton(planet_name, callback_data=data))
    elif questionNum == 2:
        resources = {planet['resource'] for planet in player[userId]['loc'].values() if planet['resource']}
        correctAnswer = randomPlanet['resource']
        for resource in resources:
            data = f'question,{resource == correctAnswer}, {questionNum}'
            keyboard.add(
                telebot.types.InlineKeyboardButton(resource, callback_data=data))

    # генерация вопроса
    text = questions[str(questionNum)](randomPlanet['planet'])
    keyboard.add(telebot.types.InlineKeyboardButton('вернуться назад', callback_data='back'))
    bot.edit_message_text(text, chatId, player[userId]['msgId'], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('deadlyGame'))
def risk_answer(call):
    chatId = call.message.chat.id
    userId = call.from_user.id

    num = random.randint(1, 10)
    selectedNum = call.data.removeprefix('deadlyGame')
    if selectedNum == str(num):
        text = ('Ты - воплощение удачи и благополучия во вселенной! Твои путешествия всегда проходят успешно. Твоя '
                'удачливость настолько велика, что кажется, будто сама Вселенная подстраивается под твои планы. Твоя '
                'удача - это не просто случайность, это дар, данный тебе свыше. Ты - истинный мастер своей судьбы, '
                'и твой успех вдохновляет всех вокруг тебя. Мы отдаём тебе 500 топлива')
        # Обновляем кол-во топлива
        player[userId]['gold'] += 500
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton('Продолжить игру', callback_data='back'))
        bot.edit_message_text(text, chatId, player[userId]['msgId'], reply_markup=keyboard)
    else:
        endGame(userId)
        text = ('Ты, рискнул своей жизнью и проиграл. Твоя неудача стала не только твоим личным позором, но и позором '
                'для всей Вселенной. Теперь ты обречен на смерть. Твоя казнь станет напоминанием для всех о том, '
                'что риск и азарт могут иметь трагические последствия.\nПопробуйте сыграть ещё раз. Для этого введите '
                'команду /game')
        bot.edit_message_text(text, chatId, player[userId]['msgId'])


def playDeadlyGame(chatId, userId):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=5)
    # Создаем первый ряд кнопок
    row1 = []
    for i in range(1, 6):
        row1.append(telebot.types.InlineKeyboardButton(text='❓', callback_data=f'deadlyGame{str(i)}'))
    # Добавляем первый ряд кнопок в объект InlineKeyboardMarkup
    keyboard.row(*row1)

    # Создаем второй ряд кнопок
    row2 = []
    for i in range(6, 11):
        row2.append(telebot.types.InlineKeyboardButton(text='❓', callback_data=f'deadlyGame{str(i)}'))
    # Добавляем второй ряд кнопок в объект InlineKeyboardMarkup
    keyboard.row(*row2)
    text = ('Местные жители предлагают тебе сыграть в смертельную игру, где ставкой является твоя жизнь.\nГотов ли ты '
            'рискнуть всем? Если да, выбери кнопку. Выигрышная только одна.\nВ случае выигрыша ты получишь 500 '
            'топлива и славу самого удачливого героя вселенной.\nВ случае проигрыша позорную смерть.')
    bot.edit_message_text(text, chatId, player[userId]['msgId'], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('getFuel'))
def handlerTradeFuel(call):
    global player
    chatId = call.message.chat.id
    userId = call.from_user.id
    _, fuelPurchased, goldSpent = call.data.split(',')
    player[userId]['fuel'] += int(fuelPurchased)
    player[userId]['gold'] = int(goldSpent)
    startTrip(chatId, userId)


def tradeFuel(chatId, userId):
    # TODO изменить с учётом слабости
    # также учесть tradePenalty
    keyboard = telebot.types.InlineKeyboardMarkup()
    currentLocation = player[userId]['loc'][str(player[userId]['currentPlanetNumber'])]
    # проверяем возможность совершить покупку
    if player[userId]['gold'] >= currentLocation['fuelCost']:
        availablePurchase = player[userId]['gold'] // currentLocation['fuelCost']
        goldRest = player[userId]['gold'] % currentLocation['fuelCost']
        text = f'Сейчас {getCurGoldAndFuel(userId)}.\nНа этой планете курс продажи 1 топливо = {currentLocation["fuelCost"]} золото.\nТопливо доступное для покупки: {availablePurchase}.'
        keyboard.add(telebot.types.InlineKeyboardButton(f'Купить топливо: {availablePurchase}',
                                                        callback_data=f'getFuel,{availablePurchase},{goldRest}'))
    else:
        text = f'Сейчас {getCurGoldAndFuel(userId)}.\nНа этой планете курс продажи 1 топливо = {currentLocation["fuelCost"]} золото.\nВашего золота недостаточно для покупки.'

    keyboard.add(telebot.types.InlineKeyboardButton('Вернуться назад', callback_data='back'))
    bot.edit_message_text(text, chatId, player[userId]['msgId'], reply_markup=keyboard)


def stealFuel(chatId, userId, callId):
    currentPlanet = player[userId]['loc'][str(player[userId]['currentPlanetNumber'])]
    winChance = 10
    lootChance = 1
    if 'steal' in currentPlanet['weakness']:
        winChance *= 3
    if player[userId]['name'] == 'проворность':
        winChance *= 2.5
        lootChance *= 3
    # При успешном ограблении
    if random.randint(1, 100) <= winChance:
        # количество топлива увеличивается
        loot = random.randint(1 * lootChance, 3 * lootChance)
        player[userId]['fuel'] += loot
        bot.answer_callback_query(callId, f'Вы успешно совершили кражу и получили {loot} топлива', show_alert=True)
    # При неуспешном ограблении
    else:
        # отобрали всё золото
        player[userId]['gold'] = 0
        # отобрали половину топлива
        player[userId]['fuel'] = player[userId]['fuel'] // 2
        player[userId]['tradePenalty'] += 1
        bot.answer_callback_query(callId, f'Вас поймали на краже, и отобрали всё золото и половину топлива.\nВсе '
                                          f'теперь знают вас как вора, теперь цены на топливо для вас дороже на 1 '
                                          f'золото.', show_alert=True)
    startTrip(chatId, userId)


def takeFuelByForce(chatId, userId, callId):
    currentPlanet = player[userId]['loc'][str(player[userId]['currentPlanetNumber'])]
    winChance = 10
    lootChance = 1
    if 'takeByForce' in currentPlanet['weakness']:
        winChance *= 3
    if player[userId]['name'] == 'мощь':
        winChance *= 3
        lootChance *= 2
    # При успешном налёте
    if random.randint(1, 100) <= winChance:
        # количество топлива увеличивается
        loot = random.randint(1 * lootChance, 3 * lootChance)
        player[userId]['fuel'] += loot
        bot.answer_callback_query(callId, f'Вы успешно отобрали топливо у местных жителей и получили {loot} топлива',
                                  show_alert=True)
        startTrip(chatId, userId)
    # При неуспешном налёте
    else:
        # отобрали всё золото
        player[userId]['gold'] = 0
        # отобрали половину топлива
        player[userId]['fuel'] = player[userId]['fuel'] // 2
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton('Вернуться назад', callback_data='back'))
        text = f'Вы не смогли отобрать топливо силой.\nРазьярённый народ расы {currentPlanet["species"]} испортил ваш корабль и теперь на все путешествия вам придётся тратить на 1 единицу топлива больше.\nТакже у вас отобрали всё золото и половину топлива.'
        bot.edit_message_text(text, chatId, player[userId]['msgId'], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data in actions)
def handlerAction(call):
    chatId = call.message.chat.id
    userId = call.from_user.id
    # Если игрок выбрал отправиться на другую планету
    if call.data == 'move':
        # Проверить список доступных планет
        checkAllowedPlanet(userId)
        # Показать список планет для передвижения
        displayMoveVariants(chatId, userId)
    # Если игрок выбрал ответить на вопрос
    elif call.data == 'answer':
        askQuestion(chatId, userId)
    # Если игрок выбрал сыграть в рисковую игру
    elif call.data == 'risk':
        playDeadlyGame(chatId, userId)
    # Если игрок выбрал купить топливо
    elif call.data == 'buy':
        tradeFuel(chatId, userId)
    # Если игрок выбрал украсть топливо
    elif call.data == 'steal':
        stealFuel(chatId, userId, call.id)
    # Если игрок выбрал отобрать топливо силой
    elif call.data == 'takeByForce':
        takeFuelByForce(chatId, userId, call.id)


def startTrip(chatId, userId):
    keyboard = telebot.types.InlineKeyboardMarkup()
    for action in actions:
        keyboard.add(telebot.types.InlineKeyboardButton(actions[action], callback_data=action))
    # Получаем текущую планету
    currentPlanet = player[userId]["loc"][str(player[userId]["currentPlanetNumber"])]
    currentPlanetName = currentPlanet["planet"]
    isAboutPlanet = int(player[userId]["currentPlanetNumber"]) > 8
    textFromLoc = currentPlanet['text'] if isAboutPlanet else f'На планете обитает раса {currentPlanet['text']}'
    textValues = f'Вы находитесь на планете {currentPlanetName}\n{textFromLoc}\nВ вашем корабле:\n{getCurGoldAndFuel(userId)}.\n'
    text = 'Ваши действия:'
    bot.edit_message_text(textValues + text, chatId, player[userId]['msgId'], reply_markup=keyboard)


# Пометка планеты посещённой
def checkVisitedPlaner(chatId, planet):
    for location in player[chatId]['loc'].values():
        if location['planet'] == planet:
            location['isVisited'] = True


# Помечаем на какой планете сейчас находимся
def checkCurrentPlanetNumber(chatId, num):
    global player
    player[chatId]['currentPlanetNumber'] = num


# Выбираем случайную расу и планету из списка
def randomChoiceSpeciesAndBirthPlace(userId):
    global player
    # Выбираем случайное число от 1 до 8
    birthPlanetNumber = random.randint(1, 8)
    # Создаём переменную со случайной планетой
    birthPlace = game_locations[userId][str(birthPlanetNumber)]
    # Добавляем в место рождения номер планеты
    birthPlace.update({'planetNumber': birthPlanetNumber})
    # Присваиваем в место рождения игрока словарь со случайной планетой
    player[userId]['birthPlace'] = birthPlace
    # Пометка планеты рождения посещённой
    checkVisitedPlaner(userId, birthPlace['planet'])
    # Помечаем текущую планету
    checkCurrentPlanetNumber(userId, birthPlanetNumber)


# Назначаем цены на топливо
def setFuelPrice(userId):
    global player
    ratio = 1
    if player[userId]["name"] == players['player3']['name']:
        ratio = 2
    for i in range(1, 9):
        player[userId]['loc'][str(i)]['fuelCost'] = random.randint(int(2 / ratio), int(6 / ratio))


# Обработка события выбора персонажа
@bot.callback_query_handler(func=lambda call: call.data in players)
def initPlayer(call):
    global player
    chatId = call.message.chat.id
    userId = call.from_user.id
    # Инициализация объекта player для конкретного пользователя
    player[userId].update(deepcopy(players[call.data]))
    player[userId].update({'loc': game_locations[userId], 'gold': 0, 'fuel': 3, 'fuelPenalty': 0, 'tradePenalty': 0})
    # Выбираем случайную расу и планету из списка
    randomChoiceSpeciesAndBirthPlace(userId)
    # Назначаем цены на топливо
    setFuelPrice(userId)
    answer = f'Вы выбрали специализацию {player[userId]["name"]}. Ваша раса {player[userId]["birthPlace"]["species"]}.'
    bot.edit_message_text(answer, chatId, player[userId]['msgId'])
    # Начало путешествия
    startTrip(chatId, userId)


# Настраиваем стартовую локацию
def adjustLocation(userId):
    global game_locations
    # Перемешиваем значения planets и присваиваем их в новую переменную
    temp_planets = list(deepcopy(planets).values())
    shuffledPlanets = temp_planets[:8]
    random.shuffle(shuffledPlanets)
    shuffledPlanets += temp_planets[8:]
    # Объединяем перемешанные значения planets и locations в один словарь game_locations
    game_locations[userId] = deepcopy(locations)
    for key, loc in game_locations[userId].items():
        loc.update(shuffledPlanets[int(key) - 1])


# Команда для начала игры
@bot.message_handler(commands=['game'])
def game(msg):
    global player
    chatId = msg.chat.id
    userId = msg.from_user.id
    # Проверяем начинал ли пользователь игру
    if (userId in player) and ('gameIsBegin' in player[userId]):
        # Если игра начата прекращаем запуск новой игры
        if player[userId]['gameIsBegin']:
            # TODO
            # keyboard = telebot.types.InlineKeyboardMarkup()
            # keyboard.add(telebot.types.InlineKeyboardButton('вернуться назад', callback_data='back'))
            # bot.edit_message_text('игра уже начата', chatId, player[userId]['msgId'], reply_markup=keyboard)
            return
    else:
        # удаляем данные прошлой игры и отмечаем что игра уже идёт
        player[userId] = {
            'gameIsBegin': True
        }
    player[userId]['gameIsBegin'] = True
    # Настраиваем стартовую локацию
    adjustLocation(userId)
    # Создаем клавиатуру
    keyboard = telebot.types.InlineKeyboardMarkup()
    # Создаем кнопки для выбора аватара
    button = []
    for i in players:
        button.append(telebot.types.InlineKeyboardButton(players[i]['name'], callback_data=i))
    keyboard.add(*button)
    # Отправляем сообщение с кнопками
    msgBot = bot.send_message(chatId, f'{greeting} \nВыберите специализацию:', reply_markup=keyboard)
    player[userId]['msgId'] = msgBot.message_id


# Команда для старта бота
@bot.message_handler(commands=['start'])
def start(msg):
    chatId = msg.chat.id
    userId = msg.from_user.id
    if (userId in player) and ('gameIsBegin' in player[userId]):
        # TODO handle
        print('aaaaaaaaaaaaaaa')
    else:
        bot.send_message(msg.chat.id, f'Привет! Если хочешь сыграть, введи команду /game')


if __name__ == '__main__':
    bot.infinity_polling()
