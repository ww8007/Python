from tkinter import *

def callback():
    bt["text"]="버튼이 클릭 되었음"

window = Tk()
bt = Button(window, text="클릭", command=callback)
bt.pack(side=LEFT)

window.mainloop()