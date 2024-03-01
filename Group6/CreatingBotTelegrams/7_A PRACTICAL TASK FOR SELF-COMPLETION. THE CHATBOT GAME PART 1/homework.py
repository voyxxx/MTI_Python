import copy

# class makeUsers:
#   def __init__(self, name, age, favorites):
#     self.name = name
#     self.age = age
#     self.favorites = favorites

#   def __str__(self):
#     return 'dsfhldsi'

# user1 = makeUsers("Alex", 32, {"colors": ["red", "green"], "food": ["apple", "banana"]})
# user2 = makeUsers("Iren", 17, {"colors": ["blue", "yellow"], "food": ["cherry", "mango"]})
# user3 = makeUsers("Vlad", 16, {"colors": ["black", "white"], "food": ["strawberry", "pineapple"]})

# users = {
#   user1: user1,
#   user2: user2,
#   user3: user3
# }

users = {
    1: {'name': 'Alex', 'age': 32, 'favorites': {"colors": ["red", "green"], "food": ["apple", "banana"]}},
    2: {'name': 'Iren', 'age': 17, 'favorites': {"colors": ["blue", "yellow"], "food": ["cherry", "mango"]}},
    3: {'name': 'Vlad', 'age': 16, 'favorites': {"colors": ["black", "white"], "food": ["strawberry", "pineapple"]}},
}

users_copy = copy.deepcopy(users)

users_copy[2]['age'] = 100
users_copy[3]['favorites']["colors"].append("purple")

print(users, id(users))
print(users_copy, id(users_copy))