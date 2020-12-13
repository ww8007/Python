import codecs

infile = codecs.open("hi.txt", "r+", "utf-8")
str = infile.read(10)
print("읽은 문자열:", str)
pos = infile.tell()     #위치 표시자 알림
print("pos = ", pos)
#infile.seek() - > 위치 표시자 지정 함수 return 값 존재
pos = infile.seek(0)
str = infile.read(10)
print("다시 읽은 문자열", str)
infile.close()