class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

# Создаем объект
person = Person("John", 25)

# Выводим объект с помощью функции print()
print(person)