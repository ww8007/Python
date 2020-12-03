from tkinter import *

window = Tk()
t = Text(window, height = 5, width = 60)
t.pack()
t.insert(END, "텍ㅌ스트 위젯은 여러줄의 \n 텍스트를 표시할 수 있습니다.")
window.mainloop()

#텍스트는 html이나 css 스타일도 사용이 가능하다.