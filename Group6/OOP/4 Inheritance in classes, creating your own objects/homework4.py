class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        if sound: print(sound)


class Cat(Animal):
    def __init__(self, name, species, sound):
        super().__init__(name, species)
        self.sound = sound
    
    def make_sound(self):
        return super().make_sound(self.sound)
    


class Dog(Animal):
    def __init__(self, name, species, sound):
        super().__init__(name, species)
        self.sound = sound

    def make_sound(self):
        return super().make_sound(self.sound)

murzik = Cat('Мурзик', 'кот', 'Мяу')
murzik.make_sound()

pirat = Dog('Пират', 'собака', 'Гав')
pirat.make_sound()