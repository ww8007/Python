리스트 연산들

1. 연결 
    a = b + c 
2. 비교 
    print(a==b), print(a!=b)
3. 위치 
    man = ["1", "2", "3"]
    index = man.index("2")
    print(index)    
4. 존재여부
    if "2" in man:
        print("1 존재")
5. 길이
    print(len(man))
6. 삭제
    remove("인덱스 이름") = 반환값 없음
    pop(1) = 반환값 존재
7. 추가
    list.append("요소") <- 인덱스 오름차순으로 채워짐
    list.insert(1, "요소") <- 인덱스 위치 지정가능
8. 최대최소
    print(max(list))
    print(min(list))
9. 정렬
    sort() 할 시 내림차순 -> 첫번째는 사전적, 두번째는 길이로 판단
    sort(reverse=True) 

리스트의 복사

1. 깊은 복사와 얕은 복사가 존재 
    scroe = [1, 2]  
    val = score <- 얕은 복사(주소값 복사)
    val = list(score) <- 깊은 복사(새로운 객체 생성해서 넘겨줌)
2. 함수에서의 리스트
    def func(list):
        list[0] = 99
3. 리스트 함축
    수식으로만 리스트 내부를 채우는 방법
    s = [x**2 for x in range(10)]
    -> x 0 부터 9 까지 제곱으로 이루어진 리스트
    [출력식 , for 변수범위, if 조건식(참이여야 결과 반영)]
    * 조건이 없어도 리스트 생성 가능하다
    * 변수의 범위로 list내 요소 사용 가능
        list1 = [1, 2, 3]
        list2 = [x*2, for x, list1]
        print(list2) -> [2, 4, 6]