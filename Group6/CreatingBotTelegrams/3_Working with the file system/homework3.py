import telebot
from bot_token import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def textToPoll(message):
    stringArray = message.text.split('\n')
    stringCount = len(stringArray)
    if stringCount > 11 or stringCount < 3:
        bot.send_message(message.chat.id, f'Строк должно быть меньше 11 и больше 3. Вы отправили {stringCount} строк(у/и)')
    else:
        bot.send_poll(message.chat.id, stringArray[0], stringArray[1:])

if __name__ == '__main__':
    bot.polling(none_stop=True)