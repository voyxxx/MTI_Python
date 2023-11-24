from tkinter import *
import random
definitions = {
    "While": "Цикл 'while' используется для выполнения блока кода, пока условие истинно.",
    "For": "Цикл 'for' используется для итерации по элементам последовательности (например, списку или строке).",
    "If": "Условие 'if' позволяет выполнить определенный блок кода, если условие истинно.",
    "Function": "Функция - это блок кода, который можно вызывать с определенными аргументами.",
    "List": "Список - это упорядоченная коллекция элементов, которая может содержать разные типы данных.",
}


def show_random_definition():
    definition_text['text'] = ''
    random_key = random.choice(list(definitions.keys()))
    definition_text['text'] = definitions[random_key]

window = Tk()
window.title('Определения Python')
window.geometry('400x200+1000+300')

definition_text = Label(window, text='Здесь появиться определение', wraplength=300)
definition_text.pack(pady=20)

button = Button(window, text='Показать определение', command=show_random_definition)
button.pack(pady=20)

window.mainloop()
