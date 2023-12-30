# https://tproger.ru/articles/gajd-po-magicheskim-metodam-v-python

# Повторение основ ООП

class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        
    def start_engine(self):
        print('Engine is started')
        
    def drive(self, distance):
        print(f'Driving {distance} kilometers')
        
car1 = Car('Toyota', 'camry', 'black', 2018)
car2 = Car('Honda', 'civic', 'red', 2010)

print(car2.brand)
print(car1.model)

car1.start_engine()
car2.drive(50)


# Наследование
# класс, который мы наследуем, называется суперкласс
# класс, который наследует атрибуты называется подкласс

class ElectricCar(Car):
    def __init__(self, brand, model, color, year, battery_capacity):
        super().__init__(brand, model, color, year)
        self.battery_capacity = battery_capacity
        
    def charge(self):
        print('The car is charging')
    
    def drive(self, distance):
        super().drive(distance)
        self.battery_capacity -= distance
        
electric_car = ElectricCar("Tesla", "Model S", "Black", 2021, 75)
print(electric_car.brand)  # Output: Tesla
electric_car.start_engine()  # Output: Engine started

electric_car.charge()  # Output: Charging the battery
electric_car.drive(50)  # Output: Driving 50 kilometers


# Практика

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self):
        print('The animal is eating')
        
    def sleep(self):
        print('The animal is sleeping')
        
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
        
    def purr(self):
        print("The cat is purring")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
        
    def bark(self):
        print('The dog is barking')


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan
        
    def fly(self):
        print("The bird is flying")



cat = Cat("Whiskers", 5, "Gray")
dog = Dog("Buddy", 3, "Labrador")
bird = Bird("Tweety", 1, 20)

cat.eat()  # Output: The animal is eating
dog.sleep()  # Output: The animal is sleeping
bird.fly()  # Output: The bird is flying

cat.purr()  # Output: The cat is purring
dog.bark()  # Output: The dog is barking
bird.eat()  # Output: The animal is eating