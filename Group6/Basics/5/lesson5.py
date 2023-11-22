# Списки
""" n = int(input('Введите количество значений списка: '))
spisok = []

for i in range(n):
    a = int(input('Значение списка:'))
    spisok.append(a)

print(*spisok) """

""" squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares) """

""" str = 'elevator'
newStr = str[1:4:1]
newStr2 = str[4::]
print(newStr)
print(f'newStr2: {newStr2}') """

"""
a = [1, 2, 3, 4, 5]
# отсчет элементов начинается с нуля

# Вызов конкретного элемента
print(a[0])
print(a[-1])

# Изменение элемента в списке
a[3] = 100
print(a)

# Добавление элементо в список
a.append(190) # метод append всегда добавляет новый элемент в конец списка
print(a) # 1 способ вывода
print(*a) # 2 способ вывода
print(*a, sep='/') # 3 способ вывода
"""

# Добавление элемента в любое место
""" a = [1, 2, 3, 4, 5]
a.insert(3, 24)
print(*a) """

"""
# Удаление конкретного элемента
a.pop(2)
print(*a)

# Переворачиваем список
a.reverse()
print(*a)

# Длина списка
print(len(a))
"""

# Очистка списка
""" a = [3,4,-150,1,2]
print(a)
a.clear()
print(a) """

# Ввод списков вручную
"""
n = int(input('Введите количество значений списка: '))
spisok = []

for i in range(n):
    a = int(input('Значение списка: '))
    spisok.append(a)

    i = i + 1

print(*spisok)
"""

# Ввод списка вручную через пробел
""" spisok = list(map(int, input().split()))
print(spisok) """

# Создание списков
""" 

a = [0 for i in range(3)]
print(a) """

# Генератор списков

""" squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)

squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2) """


# Строки

""" stroka = 'abcdfgh'
print(stroka[-1]) """

# stroka[3] = 'k'  строка - не изменяемый тип данных

str1 = 'Hello world. '
# str1[0] = 'R' - ошибка, неизменяемы тип
str2 = 'world peace and love'
str3 = str1 + str2

print(str3)



# Срезы

""" s1 = 'kjenrfasdkvnsa'
print(s1[0:5:2])
# x - начало среза(если ничего нет, то по умолчанию начинаем с нуля)
# y - конец среза(если ничего нет, то по умолчанию до самого конца)
# z - размер шага

print(s1[5:0:-2])

print(s1[0:5]) # без шага

print(s1[3::2])

print(s1[::2]) """