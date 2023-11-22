from tkinter import *

window = Tk()
window.title('9 beginner')
window.geometry('300x300+1000+200')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=3)
window.columnconfigure(4, weight=1)

def showInputText():
    label['text'] = entry.get()

def resetText():
    label['text'] = ''

label = Label(window)
label.grid(row=0, column=1, columnspan=3, pady=10)

entry = Entry(window)
entry.bind('<Return>', lambda event: showInputText())
entry.grid(row=1, column=1, columnspan=3, pady=10)

buttonClick = Button(window, text='Click', command=showInputText)
buttonClick.grid(row=2, column=1, padx=5)

buttonReset = Button(window, text='Reset', command=resetText)
buttonReset.grid(row=2, column=3, padx=5)


window.mainloop()
