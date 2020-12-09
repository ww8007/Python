mydic = dict()

mydic["하나"] = 1
mydic["둘"] = 2
mydic["셋"] =3

word = input("단어를 입력하시오 : ")
#mydic.get(인수를 두개 가질 수 있고 없으면 두번 째 인수 출력하게 함수 구성)
print (mydic.get(word, "없음"))