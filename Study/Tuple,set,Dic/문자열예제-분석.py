my = input("")


dic = dict()
dic["alphas"] = 0
dic["digits"] = 0
dic["spaces"] = 0
print(dic)
for i in my:
    if i.isalpha():
        dic["alphas"] +=1
    elif i.isdigit():
        dic["digits"] +=1
    elif i.isspace():
        dic["spaces"] +=1
print(dic)