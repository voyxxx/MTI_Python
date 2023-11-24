from ahk import AHK
from tkinter import * 

ahk = AHK(executable_path="F:\Programs\AutoHotKey\AutoHotkey.exe")

window = Tk()
window.title('Clicker')
window.geometry('400x200+1000+300')

LABEL_TEXT = 'млн. руб.'
rubleCount = 1


def addRuble():
    global rubleCount
    rubleCount = rubleCount + 1
    myRuble['text'] = f'{rubleCount} {LABEL_TEXT}'

def resetRuble():
    global rubleCount
    rubleCount = 1
    myRuble['text'] = f'{rubleCount} {LABEL_TEXT}'


myRuble = Label(window, text=f'{rubleCount} {LABEL_TEXT}', font= 24)
myRuble.pack(pady=20)

click = Button(window, text='Добыча', command=addRuble)
click.pack(pady=20)

reset = Button(window, text='Сброс', command=resetRuble)
reset.pack(pady=20)

window.mainloop()
