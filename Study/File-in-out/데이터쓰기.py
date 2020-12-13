import os.path

my = open("hi.txt", "w")
# 덮어쓰기 모드를 쓰기 싫을 시 os.path.isfile("파일명")
if os.path.isfile("hi.txt"):
    print("동일한 파일명 존재")
else:
    my.write("장동현 2015133035 \n")

my.close()