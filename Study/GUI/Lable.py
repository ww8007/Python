from tkinter import *

window = Tk()
photo = PhotoImage(file="Colab.png")
w = Label(window, image=photo)
w.pack()

window.mainloop()