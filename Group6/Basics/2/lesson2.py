""" f = '4'; d = 9
x = int(input('Input firest number: '))
y = input('Input second number: ') 
print(x*y) """



# a, b = map(int, input().split())
# print(int(input('input number: ')))
# a, b = input().split()

a, b = map(int, input().split())
print(a / b)

"""

print('Hello World')

a = 10

name = input('Введите свое имя: ')
print('Привет', name)


print('Привет друг', name ,'как дела', age, 'что делаешь', number)
print(f"Привет как дела {name} что делаешь {age} как настроение ")

"""

# Здесь будет переменная которая будет хранить число

# print('Hello') а вот так правильно
# print("Hello') - вот так не правильно


x = 5 # здесь число лежит в переменной
y = 'Storka' # здесь строка лежит в переменной
z = True # здесь лежит True или False в переменной

# Динамическая типизация

x = 10
x = 'Hello'


x = 5
x = 10
"""
Типы данных

integer - int - целые числа - 1, 2, 3
string - str - строки - 'stroka'
float - числа с плавающей запятой - вещественный числа - 3.14 , 2.25 , 34.1233454
boolean - bool - логический тип - True или False(0 или 1, правда или ложь)

"""

a = 'Iloveyou'
b = 4
c = a * b
print(c)

"""
Операторы

+ сложение
- вычитание
* умножение
/ деление

7 // 3 - целочисленное деление - результат 2
7 % 3 - остаток от деления - результат 1

x % 2 == 0 - условие четности числа

6/2 = 3

"""


a = 5
a = a + 10
a += 10

'''
a = int(input()) # '5' * 5 = 55555
print(a * 5)


a, b = map(int, input().split())

print(a + b)


3 + 5 = 8 True
3 - 5 = 8 False
'''

znak = input()
if znak == '+':
    result = a + b
    print(result)
elif a < b: 
    print('')

else:
    print('...')