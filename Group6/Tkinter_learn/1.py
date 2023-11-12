from tkinter import ttk, Tk, Label, Entry

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
    window = Tk()
    window.title('Знакомство')
    window.geometry('400x200+1000+300')
    window.iconbitmap(r"Group6\Tkinter_learn\forest.ico")
    paintElements(window)
    window.mainloop()

def init():
    showWindow()

if __name__ == "__main__":
    init()

