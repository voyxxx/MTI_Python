helloText = 'Привет странник, это простой калькулятор.'
operations = '+,-,*,/'
print(f'{helloText}\nДоступные типы операций: {operations.replace(",",", ")}')

while True: 
    curOperator = input('Введите тип операции: ')
    if curOperator in operations: break
     
while True: 
  try: 
    num1 = int(input('Введите первое число: '))
  except ValueError:
    print('Это не число.')
    continue
  break

while True: 
  try: 
    num2 = int(input('Введите первое число: '))
  except ValueError:
    print('Это не число.')
    continue
  break

if curOperator == '+':
    print(f'Результат {num1 + num2}')
elif curOperator == '-': 
    print(f'Результат {num1 - num2}')
elif curOperator == '*': 
    print(f'Результат {num1 * num2}')
elif curOperator == '/': 
    if num2 == 0: 
        print('На ноль делить нельзя')
    else:    
        print(f'Результат {num1 / num2}')

