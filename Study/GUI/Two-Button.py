from tkinter import *

window = Tk()

b1 = Button(window, text="첫번째 버튼")
b2 = Button(window, text="두번째 버튼")
b1.pack(side = LEFT, padx = 10)
#side 배치 조절 동서남북 가능
#padx pady 원하는 대로 픽셀 간격 변경 가능
b2.pack(side= RIGHT, padx = 10) #압축 배치 관리자
b1["text"]="ONE"    #간단하게 변경가능
b2["text"]="TWO"
window.mainloop()