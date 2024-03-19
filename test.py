# import random

# print(6/0)

""" 
operations = '+, -, *, /'
if '/' in operations:
  print('true')
"""

""" 
i = 0
while i < 5:
    i += 1
    print(f'inner cycle {i}')
print(f'after cycle {i}') 
"""

# print(~-1)

""" 
x = '1234567890'
y = 'j2'
if y in x: print('Ok')
else: print('not Ok') 
"""

# print(not 0)

""" 
try: 
  num1 = int(input('Введите первое число: '))
except ValueError:
  print('Это не число. Выходим.') 
"""

# print('0'.isnumeric())

""" 
num1 = 0
while True: 
  num1 += 1
  if num1 == 4: continue
  print(f'Это число {num1}')
    # num1 = int(input('Введите первое число: '))
    # continue
  if num1 > 5: break 
"""
""" 
str = 'asd'
print(', '.join(list(str))) 
"""
""" 
haveAnotherPerson = ['да', 'нет']
answer = 'да'
print(not answer in haveAnotherPerson) 
"""
""" 
myList = ['да', 'нет']
newList = '\\'.join(map(str, myList))
print(newList)
 """

# Перехват закрытия окна
""" from tkinter import *
 
def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")
 
root = Tk()
root.geometry("250x200")
root.attributes('-fullscreen', True)
# root.attributes("-toolwindow", True)
 
root.title("Hello METANIT.COM")
root.protocol("WM_DELETE_WINDOW", finish)
 
root.mainloop() """

""" 
import tkinter as tk

def entry_1_return_key_event(event):
    print('Enter key pressed in entry_1 widget.')

# Create the main window
window = tk.Tk()
window.title("PythonExamples.org")
window.geometry("300x200")

label = tk.Label(window, text="Enter input")
label.pack()

# First Entry widget
entry_1 = tk.Entry(window)
entry_1.bind('<Return>', entry_1_return_key_event)
entry_1.pack()

# Run the application
window.mainloop() 
"""

""" 
from tkinter import *

root= Tk()
root.title()
root.geometry('600x200')

def on_button_click(event):
    input_text=ent.get()
    lab=Label(text='Вы ввели : ' + input_text )
    lab.grid(row=0,column=0)
def clear_button():
    ent.delete(0, END)
ent=Entry(root)
ent.grid(row=1, column=0)
ent.bind('<Return>', on_button_click)

button_clear=Button(root, text='Очистить', command=clear_button)
# button_main=Button(root, text="Подтвердить", command=on_button_click)
button_clear.grid(row=2, column=1)
# button_main.grid(row=2, column=0)

root.mainloop() 
"""

""" 
import tkinter as tk


class Frame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=300, height=200)
        self.setupUI()

    def setupUI(self):
        self.hello_label = tk.Label(self, text="Привет, мир!", font="Times 16", padx=20, pady=25)
        self.input_text = tk.Entry(self, border=3, font="Times 14")
        self.answer_text = tk.Label(self, pady=1)
        self.button_print = tk.Button(self, text="Вывести", width=15, height=2, command=lambda: self.answer_text.config(text=self.input_text.get()))
        self.button_clear = tk.Button(self, text="Очистить", width=15, height=2, command=self.clear_input)
        self.input_text.focus()
        for element in [self.hello_label, self.input_text, self.answer_text]:
            element.pack()
        for i, button in enumerate([self.button_print, self.button_clear]):
            button.place(relx=0.3 + (0.45 * i), rely=0.75, anchor="center")

    def clear_input(self):
        self.answer_text.config(text='')
        self.input_text.delete(0, "end")

if __name__ == '__main__':
    app = tk.Tk(className="Базовый уровень")
    app.geometry("300x200")
    Frame(app).pack(expand=True, fill='both')
    app.mainloop()
     """

""" 
from tkinter import ttk, Tk

def inputAnswer(event, label):
    print(event)
    print(event.widget.get())  # Получаем введенное значение
    label.config(text=event.widget.get())  # Устанавливаем текст метки

def paintElements(root):
    question = ttk.Label(root, text='Сколько вам лет?')
    question.pack()

    answer_label = ttk.Label(root, text='')
    answer_label.pack(anchor='n', padx=8, pady=8)

    entry = ttk.Entry(root)
    entry.pack(anchor='n', padx=8, pady=8)
    entry.bind('<Return>', lambda event, label=answer_label: inputAnswer(event, label))

def showWindow():
    window = Tk()
    window.title('Знакомство')
    window.geometry('400x200+1000+300')
    paintElements(window)
    window.mainloop()

if __name__ == "__main__":
    showWindow()
 """

""" text = ''
print(len(text)) """

""" 
arr = [4,7,9]
arr.reverse()
myCount = arr.count(4)
print(arr)
print(myCount)
 """

""" x = 5
arr = [x for x in range(10)]
print(arr) """

""" arr = [1,,3] # exception
print(arr) """

""" mySet = {1,2}
print(mySet) """

""" s1 = set()
s2 = s1
s2.add(7)
print(s1) """

""" my_tuple = (1, 2, 3, 2) 
print(my_tuple.count(2)) # Output: 2 
print(my_tuple.index(3)) # Output: 2 
print(my_tuple[0]) # Output: 1
print(my_tuple + (4, 5)) # Output: (1, 2, 3, 2, 4, 5) 
print(my_tuple * 2) # Output: (1, 2, 3, 2, 1, 2, 3, 2) """

# student = {'имя': 'Иван', 'возраст': 20, 'курс': 'Python'}
# print(student.get('name'))


# print(random.randint(1, 2)) # 1 or 2

# for i in range(1, 9):
#     print(i)

# i = 5 // 2
# rest = 5 % 2
# print(i)
# print(rest)
