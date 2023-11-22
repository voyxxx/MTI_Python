my_dict = dict()

my_dict['name'] = 'John'
my_dict['age'] = 25
my_dict['city'] = 'New York'

print(my_dict)

my_dict['age'] = 26
my_dict['email'] = 'john@example.com'

prefixToAnswer = '' if 'country' in my_dict.keys() else 'не'
print(f'Ключ country в словаре my dict {prefixToAnswer} найден')

for key, value in my_dict.items():
    print(f'Ключ {key}, Значение: {value}')