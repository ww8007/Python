mydic= dict()

mydic["one"] = "하나"
mydic["two"] = "둘"
mydic["three"] = "셋"

while True:
    get = input("단어를 입력하시오")
    if get == "one":
        print(mydic[get])
    elif get == "two":
        print(mydic[get])
    elif get == "three":
        print(mydic[get])
    else:
        print("없음")