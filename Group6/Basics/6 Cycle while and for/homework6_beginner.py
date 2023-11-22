txt = input('Введите число: ')
    
try:
    num = int(txt) + 1
    for i in range(num):
        print(i)
except ValueError:
    print('Вы ввели не подходящее значение.')
