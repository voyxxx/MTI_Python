# f = open('file.txt')
# print(f.readline())
path = './Group6/OOP/5 read and write file/'
f = open(f'{path}file.txt', 'w')
f.write('one - 1 - I\ntwo - 2 - II\nthree - 3 - III\nfour - 4 - IV\nfive - 5 - V')


# Работа с файлами на Python

# Вся работа с файлами организована с помощью функции open()
# У этой функции есть два аргумента - имя файла и режим работы с файлом

'''
Режимы работы с файлами

'r'(read) - режим чтения файлов. Если второй аргумент в функции open() не указан,
            то этот режим будет работать по умолчанию
'w'(write) - режим записи в файл.
'a'(append) - режим дозаписи в конец файла
'x'(exclusive creation) - режим эксклюзивного создания файла
'b'(binary) - режим работы с файлом в двоичном режиме
't'(text) - режим работы с файлом в текстовом режиме(по умолчанию включен)
'+'(read and write) - режим чтения и записи в файл


f = open(f'{path}file.txt', 'w')
f.write('Hello, World!')
f.close()

f = open(f'{path}file.txt')
data = f.read()
print(data)
f.close()



f = open(f'{path}file.txt')
print(f.read(10))
print(f.read())


f = open(f'{path}file.txt')
print(f.readline()) # метод readline() выводит построчно текст из файла


f = open(f'{path}file.txt')
print(f.readlines())



for i in open(f'{path}file.txt'):
    print(i)


nums = []
for i in open(f'{path}file.txt'):
    nums.append(i[:-1])

print(nums)


# Запись в файл

l = ['three', 'four']
f = open('newdata', 'w')
f.write('one')
f.write('two')
f.writelines(l) # записывает список в файл

f.close()
print(f.closed)
'''

"""
Обработка исключений

try - блок кода, который может вызвать исключение
except - блок кода, который будет выполнен, если в try возникло исключение
else - блок кода, который будет выполнен, если исклоючения не возникло
finally - блок кода, который будет выполнен в любом случае

"""
"""
try:
    # Открытие файла для чтения
    f = open(f'{path}fil.txt', 'r')


    # Чтение данных из файла
    data = f.read()
    print(data)


    # Закрытие файла
    f.close()
except FileNotFoundError:
    print("Файл не найден")
except PermissionError:
    print("Нет доступа к файлу")
except Exception as e:
    print("Произошла ошибка:", str(e))

print(2 + 3 - 7)
"""