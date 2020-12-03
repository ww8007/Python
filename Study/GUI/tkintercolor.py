from tkinter import *
# from tkinter colorchooser import *
#직관적 코드
window = Tk()
bt = Button(window, text="버튼을 클릭하세요")
bt.pack()

bt["fg"]="yellow" #ff0000
bt["bg"]="green" #16진수로도 표현이 가능하다.
# color1 = askcolor()
# color2 = askcolor()

# butoon["fg"]=color1[1]
# butoon["bg"]=color2[1]
window.mainloop()