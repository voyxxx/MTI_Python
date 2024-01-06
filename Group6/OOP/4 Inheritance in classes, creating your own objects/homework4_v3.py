class Animal:
    def __init__(self, name, species, sound = None):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        if self.sound: print(self.sound)


class Cat(Animal):
    pass


class Dog(Animal):
    pass

murzik = Cat('Мурзик', 'кот', 'Мяу')
murzik.make_sound()

pirat = Dog('Пират', 'собака', 'Гав')
pirat.make_sound()