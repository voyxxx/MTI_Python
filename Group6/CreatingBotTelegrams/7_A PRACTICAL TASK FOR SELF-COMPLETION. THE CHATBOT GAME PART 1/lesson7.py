# Словарь
# Изменяемый
# Упорядоченный
# пары ключ: значение
# ключ - уникальный, (int, str, tuple, float, bool) неизменяемый тип данных
# значение - любое


# d = {
#     'cat': 'кот', 
#     'dog': 'собака'
# }

# print(d)

# users = {
#     1: {'name': 'Ivan', 'age': 32},
#     2: {'name': 'Milana', 'age': 17}
# }

# print(users[1]['name'])

# # добавление
# users[3] = {'name': "Vlad", 'age': 16}
# print(users)

# # удаление
# del users[1]
# users.pop(2)
# print(users)

# Списки
# Изменяемый
# Упорядоченный
# Набор данных

# pets = ['Murka', 'Bobik']

# # добавление
# pets.append('Murzic')
# pets.insert(1, 'Homa')
# print(pets)

# # удаление
# pets.pop(0)
# pets.remove('Bobik')
# print(pets)

# users = {
#     1: {'name': 'Ivan', 'age': 32, 'pets': [{'type': 'cat', 'name': 'Murzic'},
#                                             {'type': 'dog', 'name': 'Bobik'}]},
#     2: {'name': 'Milana', 'age': 17, 'pets': [{'type': 'cat', 'name': 'Murka'},
#                                               {'type': 'hamster', 'name': 'Homa'}]}
# }

# # print(users[1], users[2['name]])
                                
# print(users[1]['name'])
# print(type(users))

# for user in users:
#     print(users[user]['name'])

# print(*[users[user]['name'] for user in users], sep='\n')

# print(*users)
# # Потом вывести имена владельцев и их животных
# for user in users:
#     print(f"{users[user]['name']}'s pets:")
#     for pet in users[user]["pets"]:
#         print(f"\t{pet['type']} {pet['name']}")


# КОПИИ

# поверхностная копия
# users = {
#     1: {'name': 'Ivan', 'age': 32},
#     2: {'name': 'Milana', 'age': 17}
# }

# users_1 = users 
# users_1[1] = {'name': 'Misha', 'age': 32}

# print(users, id(users))
# print(users_1, id(users_1))

# поверхностная копия 
# import copy

# users = {
#     1: {'name': 'Ivan', 'age': 32},
#     2: {'name': 'Milana', 'age': 17}
# }

# users_2 = copy.copy(users)
# # все ок
# users_2[1] = {'name': 'Misha', 'age': 32}
# print(users, id(users))
# print(users_2, id(users_2))

# # не ок
# users_2[1]['age'] = 12
# print(users, id(users))
# print(users_2, id(users_2))

# глубокая копия
# import copy

# users = {
#     1: {'name': 'Ivan', 'age': 32},
#     2: {'name': 'Milana', 'age': 17}
# }

# users_2 = copy.deepcopy(users)

# все ок
# users_2[1] = {'name': 'Misha', 'age': 32}
# print(users, id(users))
# print(users_2, id(users_2))

# все ок
# users_2[1]['age'] = 12
# print(users, id(users))
# print(users_2, id(users_2))