from tkinter import *

window = Tk()
#라벨을 그냥 설명 같은 느낌
lab = Label(window, text="안녕하세요")
lab.pack()
#버튼은 클릭 가능 gui
bt=Button(window, text="tkinter로 버튼을 쉽게 만들 수 있습니다.")
bt.pack()

window.mainloop()