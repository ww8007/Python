from tkinter import *

def process():
    print("안녕하세요")

window = Tk()
bt = Button(window, text="클릭", command=process)
bt.pack()

window.mainloop()