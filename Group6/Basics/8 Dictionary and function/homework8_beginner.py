my_dict = dict()

my_dict['name'] = 'John'
my_dict['age'] = 25
my_dict['city'] = 'New York'

print(my_dict)

my_dict['age'] = 26
my_dict['email'] = 'john@example.com'

del my_dict['city']

for key, value in my_dict.items():
    print(f'Ключ {key}, Значение: {value}')