from tkinter import *
def show():
    print("이름: %s\n나이: %s" % (e1.get(), e2.get()))

parent = Tk()
Label(parent , text="이름").grid(row=0)
Label(parent, text="나이").grid(row=1)
#grid : 표처럼 생성 좌표로 표현가능 격자 배치 관리자
e1 = Entry(parent)
e2 = Entry(parent)

e1.grid(row=0, column=1) # (0, 1)
e2.grid(row=1, column=1) # (1, 1)
Button(parent, text='보이기', command=show).grid(row=3,
column=1, sticky=W, pady=4)
#stick : 격자 배치관리자에서 사용 w,s,e,n (n,s,e,w) 왼쪽 정렬 사용
#간격 4픽셀
parent.mainloop( )