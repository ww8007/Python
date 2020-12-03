from tkinter import *
from math import *

def cal():
    label.configure(text="결과 :" + str(eval(entry.get())))

window = Tk()

Label(window, text="파이썬 수식 입력 :").pack
entry = Entry(window)
b1 = Button(window, text="계산", command = cal)

entry.pack()

label = Label(window, text = "결과")
b1.pack(side="right")
label.pack(side="left")  
#pack은 압축 배치 관리자 : 위젯을 부모안에 압축하여 배치
window.mainloop()