exitTemplate = 'exit'
isSubsequent = False
exitText = 'Если хотите выйти введите "exit".'

while True:
    if isSubsequent:
      print(exitText)
    isOk = False
    text = input('Введите число: ')
    
    if (text == exitTemplate):
      break

    try:
        num = int(text)
        if num % 3 == 0: 
            isOk = True
            print('Число делится на 3')
        if num > 10: 
            isOk = True
            print('Число больше 10')
        if not isOk:
            print('Число не соответствует условиям')
    except ValueError:
        print('Вы ввели не число.')
        
    isSubsequent = True

