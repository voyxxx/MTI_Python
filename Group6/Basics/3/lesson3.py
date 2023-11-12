"""
Разбор ДЗ 2

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
znak = input('Введите знак арифметической операции')

if znak == '+':
    result = a + b
    print(result)
elif znak == '-':
    result = a - b
    print(result)
    
"""

# AND И
# OR  ИЛИ
# NOT НЕ

# Оператор сравнения (==)

x = 5
y = 8

result = x == y
print(result)

# Оператор неравенства (!=)

x = 5
y = 8

result = x != y
print(result)

# Операторы сравнения

# > большн
# < меньше
# >= больше или равно
# <= меньше или равно

age = 25

result = age >= 18
print(result)  # Вывод: True

# Оператор И - строгий логический оператор (and)

is_raining = True
has_umbrella = False

take_umbrella = is_raining and has_umbrella
print(take_umbrella)  

a = 4

result = (a < 20) and (a > 5)
print(result)

# Оператор ИЛИ - не строгий логический оператор (or) 

a = 4

result = (a < 20) or (a > 5) 
print(result)

# Приоритет логических операторов


# 1 - NOT
# 2 - AND
# 3 - OR

x = 5
y = 10
z = 15

result = x < y and y < z or x == z
print(result)  # Вывод: True

# Комбинирование логических операторов

x = 5
y = 10
z = 15


print((x > 0 and y < 20) or z == 15) # True

print(not(x > 0 and y < 20)) # False

print(x > 0 and (y < 20 or z == 15)) # True

x = 5
y = 10

print(x == y) # False
print(x != y) # True
print(x > y) # False
print(x < y) # True
print(x >= y) # False
print(x <= y) # True

# False - 0, 0.0, [] пустой список,'' пустая строка, {} пустой словарь, set() пустое множество
# True - все остальное

x = 5
y = 0
z = ''

print(bool(x))
print(bool(y))
print(bool(z))

# Операторы сравнения цепочкой

x = 5
y = 10
z = 15

result = x < y < z
print(result)


# Тернарный условный оператор

x = 5 

result = 'Число больше 10' if x > 10 else 'Число меньше 10'
print(result)

if x > 10:
    print('Число больше 10')
else:
    print('Число меньше 10')