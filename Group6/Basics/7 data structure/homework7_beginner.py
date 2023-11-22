myTuple = (777, 42, 2000)
myEnum = ('Первое', 'Второе', 'Третье')
print(f'Кортеж: {myTuple}')

sum = 0

for idx, value in enumerate(myTuple):
    print(f'{myEnum[idx]} число: {value}')
    sum += value

print(f'Сумма: {sum}')