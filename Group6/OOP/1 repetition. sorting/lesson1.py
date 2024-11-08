# Структуры данных

'''
Список - коллеция упорядоченных элементов
Каждый элемент списка имеет индекс, индексация начинается с нуля
В списках могут быть разные типы данных
Список - изменяемая структура данных

'''

a = [1, 3, 2, 6, 5, 8, 4]
a[-1] = 1667
a.append(123)
print(a)








'''
Кортеж - коллекци упорядоченных элементов, при этом неизменяемая

'''
my_tuple = (1, 2, 4, 6, 2, 1)

'''
Словари - набор пар ключ-значение
Все ключи в словаре - уникальные
Словари - изменяемый тип данных

'''
my_dict = {'Иванов' : '5', 'Сидоров' : '4', 'Егоров' : '2'}

my_dict['Петров'] = '5'

print(my_dict)

a = my_dict.keys()
print(a)

'''
Множества - неупорядоченная коллекция уникальных элементов
У элементов множества нет индексов, но все элементы - уникальные, повторений нет

'''

set1 = {1, 2, 3}
set2 = {3, 5, 6} # разность этих множеств = {1, 2}


# Пузырьковая сортировка

'''
Принцип работы пузырьковой сортировки:
1. Сравниваем первый элемент списка с вторым.
2. Если первый элемент больше второго, то меняем их местами.
3. Переходим ко второму и второму элементу и сравниваем их, и так далее, пока не достигнем конца списка.
4. После первой итерации самый большой элемент окажется в конце списка.
5. Повторяем этот процесс для оставшихся элементов, и каждый раз самый большой элемент "всплывает" на своё место.
6. Повторяем процесс до тех пор, пока список не станет упорядоченным.


'''


def bubble_sort(arr):
    n = len(arr)
    
    # Проходим по каждому элементу массива
    for i in range(n):
        # Последние i элементов уже отсортированы,
        # поэтому мы можем их пропустить
        for j in range(0, n-i-1):
            # Если текущий элемент больше следующего,
            # меняем их местами
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print(sorted_arr)


# Сортировка выбором

'''
Принцип работы сортировки выбором:
1. Проходим по списку и находим наименьший элемент.
2. Обмениваем этот элемент с первым элементом в списке (если сортируем по возрастанию) или наибольший элемент с последним элементом (если сортируем по убыванию).
3. Продолжаем поиск наименьшего (или наибольшего) элемента среди оставшихся элементов и повторяем процесс обмена.
4. Повторяем этот процесс для каждой позиции в списке, пока не достигнем конца списка.

'''

def selection_sort(arr):
    n = len(arr)
    
    # Проходим по каждому элементу массива
    for i in range(n):
        # Находим индекс минимального элемента
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Меняем местами текущий элемент с минимальным
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = selection_sort(arr)
print(sorted_arr)


# Сортировка вставками

'''
Принцип работы сортировки вставками:
1. Считаем первый элемент списка отсортированным.
2. Затем берем следующий элемент и вставляем его на правильное место в уже отсортированной части списка.
3. Повторяем этот процесс для каждого элемента, пока весь список не будет отсортирован.


'''

def insertion_sort(arr):
    n = len(arr)
    
    # Проходим по каждому элементу массива
    for i in range(1, n):
        key = arr[i]
        j = i-1
        
        # Сдвигаем все элементы больше ключа на одну позицию вперед
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        # Вставляем ключ в правильное место
        arr[j+1] = key
    
    return arr

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = insertion_sort(arr)
print(sorted_arr)


# Сортировка встроенными методами Python

# Функция sorted не изменяет исходный список. Это функция создает новый отсортированный список
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = sorted(arr)
print(sorted_arr)

# Функция Sort сразу сортирует исходный список. Отсортированный список вернуть в прежний вид нельзя
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
arr.sort()
print(arr)


# Сортировка словаря по ключам
d = {'apple': 10, 'orange': 20, 'banana': 5, 'peach': 15}
sorted_d = dict(sorted(d.items()))
print(sorted_d)


# Сортировка множества
s = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}
sorted_s = sorted(s)
print(sorted_s)