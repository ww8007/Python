dic = dict()

dic["B4"] = "Before"
dic["TX"] = "Thanks"
dic["BBL"] = "Be Back Later"
dic["BCNU"] = "Be Seeing You"
dic["HAND"] = "Have A Nice Day"

a = input("번역할 문장을 입력하시오. : ")
a = a.split()
result = ""
for i in a:
    if i in dic:
        result += dic.get(i) + " "
    else:
        result += i + " "

print(result)


