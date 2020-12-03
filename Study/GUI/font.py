from tkinter import *

def Bigfont():
    global size
    size += 10
    label.configure(font=("Helvetica", size))

def Smallfont():
    global size
    size -=10
    label.configure(font=("Helvetica",size))

size = 20
window = Tk()

label = Label(window, text = "Hello world", font = ("Helvetica", size))
bigger = Button(window, text ="폰트를 크게", command= Bigfont)
smaller = Button(window, text = "폰트를 작게", command=Smallfont)

label.pack()
bigger.pack()
smaller.pack()

window.mainloop()