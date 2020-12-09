#딕셔너리 선언
mydic = {"가" : 1, "나" : 2, "다" : 3}
print(mydic)
print(mydic.get("가"))

mydic["다"] = 5     #값 대입
mydic["라"] = 6     #값 추가
a= mydic.pop("가")  #삭제 값 반환

print(mydic)
print(a)            #반환값 출력