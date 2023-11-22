from tkinter import *
import time

tk = Tk()
tk.title('Clicker')
tk.geometry('1000x550')
n = 0
start_time = time.time()

def nplus():
    global n
    n += 1
    label['text'] = str(n) + '₽'

def nreset():
    global n, start_time
    n = 0
    start_time = time.time()
    label['text'] = str(n) + '₽'
    update_timer()


def update_timer():
    current_time = int(time.time() - start_time)
    timer_label['text'] = f'Прошло времени: {current_time} сек'
    tk.after(1000, update_timer)

btn1 = Button(text='CLICK', background='#238', foreground='#111',
              padx='20', pady='8', font='16', command=nplus)
btn1.pack()

label = Label(tk, text=str(n) + '₽', font=('Helvetica 100'))
label.pack()

btn2 = Button(text='RESET', background='#238', foreground='#111',
              padx='20', pady='8', font='16', command=nreset)

btn2.pack()

timer_label = Label(tk, text='Прошло времени: 0 сек.', font=('Helvetiсa, 16'))
timer_label.pack(anchor='sw', padx=10, pady=10)

update_timer()
mainloop()