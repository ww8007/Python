#얕은 복사 -> 주소값만 복사와 같은 개념
score = [1,2,3,4,5]
val = score

val[3] =50 
print(score,"\n")
print(val)

#깊은 복사 -> 아예 새로운 객체 생성개념
score = [1,2,3,4,5]
val = list(score)

val[3] =50 
print(score,"\n")
print(val)


#함수안에서 새로운 객체를 생성하지 않는 이상 리스트의 변화는 남게 된다.
print ("\n")
def func(my):
    my[0] = 99

val = [1,2,3,4,5]
print(val)

func(val)
print(val)