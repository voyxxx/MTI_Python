import re

haveAnotherPerson = ['да', 'нет'] # available options for having an accompanying person
firstText = f'Введите возраст и наличие сопровождающего в формате: +0-999 {"\\".join(map(str, haveAnotherPerson))}+.\n:'

def checkAnswer(data):
    return len(data) != 2 or not data[0].isnumeric() or not data[1] in haveAnotherPerson

def inputVisitorData(isFirst = True):
    visitor = input(f'{"" if isFirst else "Неверный формат. "}{firstText}')
    return re.split(r'\s+', visitor)

visitorData = inputVisitorData()

while checkAnswer(visitorData):
    visitorData = inputVisitorData(False)

age = int(visitorData[0])
haveAccompanying = visitorData[1] == 'да'

if age < 12:
    print('Билет бесплатный')
elif 12 <= age < 18 and haveAccompanying:
    print('Билет со скидкой')
else:  
    print('Полная стоимость билета')