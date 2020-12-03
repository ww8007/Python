#버트의 텍스트 여러줄 가능
#버튼을 누르면 등록된 함수가 호출(이벤트 처리기 느낌)
#레이블은 다양한 글꼴로 텍스트를 표시가능하지만 버튼은 하나의 글꼴만 사용가능

from tkinter import *

window = Tk()

b1 = Button(window, text="이것이 파이썬 버튼입니다.")
b1.pack(side = LEFT)
#pack은 압축 배치 관리자 : 위젯을 부모안에 압축하여 배치
window.mainloop()