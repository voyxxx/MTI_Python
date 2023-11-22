from tkinter import ttk, Tk

errorText = 'Вы ввели не число, попробуйте ещё раз'

def isAdult(age): 
    return 'Вы совершеннолетний' if int(age) > 18  else 'Вы несовершеннолетний'

def checkIsNumber(age):
    try: 
        return int(age)        
    except ValueError:
        print(errorText)

def inputAnswer(event, label):
    answer = errorText
    if (checkIsNumber(event.widget.get())):
        answer = isAdult(event.widget.get())
    
    label.config(text=answer)  # Устанавливаем текст метки
    label.pack(anchor='n', padx=8, pady=8)

def paintElements(root):
    question = ttk.Label(root, text='Сколько вам лет?')
    question.pack()

    answer_label = ttk.Label(root, text='')

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