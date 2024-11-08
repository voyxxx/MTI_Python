# Структуры данных

# списки(list) - изменяемая структура. каждый элемент имеет свой индекс
'''
Упорядоченность
Изменяемость
Разнообразие типов данных
Доступ по индексу
Изменяемость элементов

'''

my_list = [1, 2, 3, 4, 'five']
my_list[2] = 193


# Кортеж(turple) - неизменяемая структура данных

""" my_tuple = (1, 2, 3, 4, 'five')
my_tuple = (1, 2, 3, 2) 
print(my_tuple.count(2)) # Output: 2 
print(my_tuple.index(3)) # Output: 2 
print(my_tuple + (4, 5)) # Output: (1, 2, 3, 2, 4, 5) 
print(my_tuple * 2) # Output: (1, 2, 3, 2, 1, 2, 3, 2) """


# Словарь(Dictionary) - представляет собой пары ключ-значение. Все ключи - уникальные

my_dict = {
    'ключ1':'значение1',
    'ключ2':'значение2',
    'ключ3':'значение3'
}

value = my_dict['ключ1']

my_dict['ключ4'] = 'значение4'

del my_dict['ключ1']

# Проверка на наличие какого-либо ключа

if 'ключ1' in my_dict:
    print('Ключ1 присутствует в словаре')

# Перебор элементов

for key, value in my_dict.items():
    print('Ключ: ', key, 'Значение: ', value)

# Множества - неупорядоченная коллекция элементов

my_set = {1, 2, 3, 4, 5}
my_set = set([1, 2, 3, 4, 5])


# Задачи по спискам

#1 Посчитать сумму элементов в списке
# вариант 1
numbers = [1, 2, 3, 4, 5]

sum_of_numbers = 0

for number in numbers:
    sum_of_numbers = sum_of_numbers + number

print(sum_of_numbers)

# вариант 2

a = [1, 2, 3]
b = [4, 5, 6]

total = sum(a) + sum(b)
print(total)

# Множества(set) - неупорядоченная коллекция уникальных элементов

my_set = {1, 2, 3, 4, 5}
my_set = set([1, 2, 3, 4, 5])

# Добавление элементов в множество

my_set.add(234)

# Удаление элементов

my_set.remove(3)

# Операции над множествами

# пересечение множеств

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.intersection(set2)
print(result)

# объединение двух множеств

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)

# Разность двух множеств

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.difference(set2)
print(result)


# Создание неизменного множества

frozen = frozenset([1, 2, 3])

# Примеры задач
#1 - Удалить из списка повторяющиеся значения

lst = [1, 2, 3, 5, 5, 1, 6, 2, 9, 2, 1]

new_lst = list(set(lst))
print(new_lst)


#2 - Написать программу, которая получает два списка и выводит список элементов, которые есть только в первом списке


def check_lists(list1, list2):
     set1 = set(list1)
     set2 = set(list2)
     result = list(set1 - set2)
     return result

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [2, 4, 6, 8, 10]
 
result = check_lists(list1, list2)
print(result)