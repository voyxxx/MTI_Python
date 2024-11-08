""" from tkinter import ttk, Tk, Label, Entry
# import tkinter as tk
# from tkinter import ttk

def inputAnswer(event, answer):
    print(event)
    print(event.entry.get())
    # answer = ttk.Label()
    # answer.pack(anchor='n', padx=8, pady= 8)
    answer["text"] = event.entry.get()

def printAnyElement(element):
    print('element ', element)
    # element["text"] = "I am in printAnyElement"

def paintElements(root): 
    question = ttk.Label(root, text='Сколько вам лет?')
    question.pack()  

    answer = ttk.Label()
    answer.pack(anchor='n', padx=8, pady= 8)

    entry = ttk.Entry(root)
    entry.pack(anchor='n', padx=8, pady= 8)
    # entry.bind('<Return>', lambda event:
                                # inputAnswer(event.entry))
    entry.bind('<Return>', inputAnswer)
    # entry.bind('<Return>', lambda e:
    #                             inputAnswer(event=e))
    
    # printAnyElement(answer)

def showWindow(): 
    window =Tk()
    window.title('Знакомство')
    window.geometry('400x200+1000+300')
    window.iconbitmap(r"Group6\Tkinter_learn\forest.ico")
    paintElements(window)
    window.mainloop()

def init():

    showWindow()
if __name__ == "__main__":
    init() """


""" import tkinter as tk


class Frame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.setupUI()

    def setupUI(self):
        self.hello_label = tk.Label(self, text="Привет, мир!", font="Times 16", padx=20, pady=25)
        self.input_text = tk.Entry(self, border=3, font="Times 14")
        self.answer_text = tk.Label(self, pady=1)
        self.button_print = tk.Button(self, text="Вывести", width=15, height=2, command=lambda: self.answer_text.config(text=self.input_text.get()))
        self.input_text.focus()
        for element in [self.hello_label, self.input_text, self.answer_text, self.button_print]:
            element.pack()


if __name__ == '__main__':
    app = tk.Tk(className="Начальный уровень")
    app.geometry("300x200")
    Frame(app).pack() 
    app.mainloop() """


""" import tkinter as tk

def change_bg_color():
    color = color_entry.get()
    root.configure(bg=color)

root = tk.Tk()
root.title("Изменение цвета окна")

# Создание виджетов
color_label = tk.Label(root, text="Введите цвет:")
color_entry = tk.Entry(root)
change_color_button = tk.Button(root, text="Изменить цвет", command=change_bg_color)

# Размещение виджетов
color_label.pack(pady=10)
color_entry.pack(pady=10)
change_color_button.pack(pady=10)

# Запуск главного цикла
root.mainloop() """

""" import tkinter as tk
from tkinter import PhotoImage

def set_gradient_bg(root, color1, color2):
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    # Создаем изображение с градиентом
    gradient = PhotoImage(width=width, height=height)
    for y in range(height):
        shade = "#{:02x}{:02x}{:02x}".format(
            int(255 - y * (255 / height)),
            int(y * (255 / height)),
            0
        )
        gradient.put(shade, (0, y))

    # Создаем холст и устанавливаем изображение
    canvas = tk.Canvas(root, width=width, height=height, borderwidth=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=gradient)

# Создаем окно
root = tk.Tk()
root.title("Градиентный фон")

# Устанавливаем градиентный фон
set_gradient_bg(root, "red", "yellow")

# Запускаем главный цикл
root.mainloop()
 """

import tkinter as tk
from random import choice


definitions = {
    "While": "Цикл 'while' используется для выполнения блока кода, пока условие истинно.",
    "For": "Цикл 'for' используется для итерации по элементам последовательности (например, списку или строке).",
    "If": "Условие 'if' позволяет выполнить определенный блок кода, если условие истинно.",
    "Function": "Функция - это блок кода, который можно вызывать с определенными аргументами.",
    "List": "Список - это упорядоченная коллекция элементов, которая может содержать разные типы данных."
}

class Frame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.setupUI()

    def setupUI(self):
        self.title_label = tk.Label(self, text="Словарик Pythonista", font="Times 18", padx=20, pady=25, fg="#15334f", bg="#214f79", width=50)
        self.definition_text = tk.Label(self, border=3, font="Times 14", width=50, height=6, bg="#43a2f9", fg="#0a1824")
        self.button_show = tk.Button(self, text="Показать определение", command=self.show_random_defition, width=50, height=3, font="Times 16", fg="#2c6ba4", bg="#3886ce")
        for element in [self.title_label, self.definition_text, self.button_show]:
            element.pack()

    def show_random_defition(self):
        fin, new, old = '', choice(list(definitions.values())), self.definition_text['text']
        while new == old.replace('-\n', ''):
            new = choice(list(definitions.values()))
        for i, s in enumerate(new):
            fin += s
            if (i + 1) % 44 == 0: 
                fin += '-\n' if s.isalpha() else '\n'
        self.definition_text.configure(text=fin)


if __name__ == '__main__':
    app = tk.Tk(className="Определение python")
    app.geometry("400x300")
    Frame(app).pack(expand=True, fill='both')
    app.mainloop()
