import tkinter as tk
from tkinter import *


root = tk.Tk()

root.title('Hello world')
root.geometry('700x500')

def on_button_click():
    label.config(text='Button clicked!')


label = Label(root, text='Привет ребята')
label.pack()


button1 = Button(root, text='Click me', command=on_button_click)
button1.pack()


button2 = Button(root, text='Click me', command=on_button_click)
button2.pack()

definition_text = tk.Text(root, width=40, height=10, wrap=tk.WORD)
definition_text.pack(pady=10)


root.mainloop()