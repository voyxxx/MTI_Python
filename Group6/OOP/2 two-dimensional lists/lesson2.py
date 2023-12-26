w = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# Создание двумерных массивов, заполненных элементами

a = 3        
mas = [0] * a # вот здесь получится список [0, 0, 0]
for i in range(a):
 mas[i] = [0] * a
print(mas)

a = 2
mas = []
for i in range(a):
 mas.append([0] * a)
print(mas) 

# Создание двумерных массивов с помощью генераторов

val = 1
(M, N) = (4, 5)
# generate a M × N matrix initialized with val
x = [[val for i in range(N)] for j in range(M)]
print(x)


# Ввод двумерного массива с клавиатуры
'''
a = int(input())
mas = []
for i in range(a):
 mas.append(list(map(int, input().split())))
print(mas)

mas = [list(map(int, input().split())) for i in range(int(input()))]

'''

# Добавление, удаление, изменение элементов в двумерном массиве


x[0].append(1)

x[0][1] = 2

x[0].remove(0) # мы указываем конкретный элемент, который хотим удалить, а не индекс


# Итерирование по двумерному массиву

def printMass (mass):
    for i in range (len(mass)):
        for j in range (len(mass[i])):
           print ( "{:4d}".format(mass[i][j]), end = "" )
   print()

def printMass (mass):
    for row in mass:
        for x in row:
           print ( "{:4d}".format(x), end = "" )
   print ()

mas = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
for i in range(0, len(mas)):
 for i2 in range(0, len(mas[i])):
     print(mas[i][i2], end=' ')
 print()


mas = [[2, 4, 7, 3], [4, 5, 6, 9], [1, 0, 4, 2], [7, 8, 4, 7]]
mas2 = []
for i in mas:
 mas2.append(sorted(i))
print(mas2)

Падение снежинки

import random
import time
import os


# Определение символов для снежинки и пустого пространства
snowflake = "🏔"
empty_space = "🎠"


# Определение высоты и ширины поля
height = 20
width = 30


# Создание пустого поля с помощью генератора
field = [[empty_space for _ in range(width)] for _ in range(height)]


# Очистка терминала
os.system("cls" if os.name == "nt" else "clear")


# Функция для отображения поля
def display_field(field):
    for row in field:
        print("".join(row))


# Отображение начального состояния поля
display_field(field)


# Периодическое обновление состояния поля и его отображение
while True:
    os.system("cls" if os.name == "nt" else "clear")
    
    # Определение случайных координат для снежинки
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    
    # Падение снежинки до дна поля
    while y < height - 1 and field[y+1][x] == empty_space:
        field[y][x] = empty_space
        y += 1
        field[y][x] = snowflake
    
    # Отображение обновленного поля
    display_field(field)
    
    # Задержка между кадрами
    time.sleep(0.1)