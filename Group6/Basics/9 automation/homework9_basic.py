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

def showPopup(): 
    if hasattr(window, '_second_window'):
        window._second_window.destroy()
    window._second_window = Toplevel(window)
    window._second_window.title('New Window')
    window._second_window.geometry('300x200')

    label = Label(window._second_window, text = entry.get())
    label.pack(pady=30)


def resetText():
    label['text'] = ''
    if hasattr(window, '_second_window'):
        window._second_window.destroy()

entry = Entry(window)
entry.bind('<Return>', lambda event: showInputText())
entry.grid(row=0, column=1, columnspan=3, pady=(60, 10))

label = Label(window)
label.grid(row=1, column=1, columnspan=3, pady=10)

buttonClick = Button(window, text='Click', command=showPopup)
buttonClick.grid(row=2, column=1, padx=5)

buttonReset = Button(window, text='Reset', command=resetText)
buttonReset.grid(row=2, column=3, padx=5)


window.mainloop()
