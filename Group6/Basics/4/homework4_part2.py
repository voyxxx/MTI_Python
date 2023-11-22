from tkinter import ttk, Tk

errorText = 'Вы ничего не ввели'

def inputAnswer(event, label):
    name = event.widget.get()
    answer = f'Привет, {name}!' if len(name) else errorText
    
    label.config(text=answer)  # Устанавливаем текст метки
    label.pack(anchor='n', padx=8, pady=8)

def paintElements(root):
    question = ttk.Label(root, text='Назовите ваше имя?')
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