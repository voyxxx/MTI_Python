
def my_decorator(func):
    def wrapper(a, b):
        print('Привет')
        print(func(a, b))
        print('Пока')
    return wrapper

@my_decorator
def rect_area(a = 0, b = 0):
    'Функция для вычисления площади прямоугольника'
    return a * b

@my_decorator
def sum_squres(a = 0, b = 0):
    return sum(i ** 2 for i in range(a, b + 1))

print(rect_area(3, 5))
print(sum_squres(1, 3))