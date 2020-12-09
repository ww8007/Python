num = {1, 2, 3}

num.add(4)

print(num)

# num.remove(0)  없는 세트 항목 삭제시 오류
# 세트는 remove 반환하지 않음
b = num.remove(1)
print(b)
print(num)
#전체삭제
num.clear()

a = {1, 2, 3}
b = {1, 2, 3}

print(a==b)
print(a > b)            #두 항목이 완전히 같더라도 포함이 아니다.
print(b.issubset(a))    #두 항목이 같으면 부분집함은 맞다.

a = {1, 2, 3}
b = {3, 4, 5}

print(a|b)              #합집합
print(a & b)            #교집합
print(a - b)            #차집합
