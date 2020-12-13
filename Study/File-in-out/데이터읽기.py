infile = open("hi.txt", "r")
#파일의 끝을 알 수 없을 때 이 방법 사용
line = infile.readline()
while line != "":
    print(line)
    line = infile.readline()
infile.close()
#오른쪽 공백 문자 제거 메소드 .rstrip()

my = open("hi.txt", "r")
for line in my:
    line = line.rstrip()
    print(line)
my.close()