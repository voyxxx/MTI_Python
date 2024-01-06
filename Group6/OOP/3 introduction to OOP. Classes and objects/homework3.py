class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f'Марка: {self.mark}, модель: {self.model}, год выпуска: {self.year}')

seven = Car('Lada', '2107', 2010)
seven.display_info()
        