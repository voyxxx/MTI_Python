niva = ['Hunter', 100, 150, 'мокрый асфальт']
lamba = ['Urus', 500, 20, 'оранжевый']

class Car:
    def __init__(self, brand, year, probeg, hp):
        self.brand = brand
        self.year = year
        self.probeg = probeg
        self.hp = hp
        
    def drive(self):
        print('Машина уехала на техосмотр')

niva = Car('Hunter', 2010, 100, 100)
lamba = Car('Urus', 2018, 20, 500)

niva.drive()

# Пример 2

class Dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
    
    def description(self):
        print(f'{self.name} is {self.age}')
        
    def speak(self, sound):
        print(f'{self.name} says {sound}')
        
buddy = Dog('Buddy', 'black', 10)
marley = Dog('Marley', 'brown', 2)

print(buddy.age)
print(marley.color)

buddy.description()
marley.description()
print(buddy)

buddy.speak('Woof woof')
marley.speak('Purrrrr')