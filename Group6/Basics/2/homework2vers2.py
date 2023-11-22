import re
import msvcrt

operations = '-+*/'
pattern = '23 * 99'
isFirst = True
isStopped = False

while True:
  helloText = f'Привет странник, это простой калькулятор. Введи пример с операторами: {", ".join(list(operations))}. Например {pattern}:\n'
  example = input(helloText) if isFirst else input()
  elements = re.split(fr'\s*([{operations}])\s*', example)
  if len(elements) == 3 and elements[2].isnumeric() and elements[0].isnumeric(): 
    break
  else:
    isFirst = False
    print(f'Введенный пример не соответствует шаблону {pattern}, попробуй ещё раз. Чтобы выйти нажми клавишу ESC')
    if(msvcrt.getch() == chr(27).encode()): 
       isStopped = True
       break

if not isStopped:
  sign = elements[1]
  num1 = int(elements[0])
  num2 = int(elements[2])

  if sign == '+':
      print(f'Результат {num1 + num2}')
  elif sign == '-': 
      print(f'Результат {num1 - num2}')
  elif sign == '*': 
      print(f'Результат {num1 * num2}')
  elif sign == '/': 
      if num2 == 0: 
          print('На ноль делить нельзя')
      else:    
          print(f'Результат {num1 / num2}')