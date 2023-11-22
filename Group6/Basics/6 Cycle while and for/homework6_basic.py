import sys

txt = input('Введите число: ')
count = 0

def output(start, to):
    i = start
    while i <= to:
        print(i)
        i += 1  

try:
    int(txt)
except ValueError:
    print('Вы ввели не подходящее значение.')
    sys.exit()

output(count, int(txt))