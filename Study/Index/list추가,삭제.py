hero = ["스파이더맨", "슈퍼맨", "베트맨"]
h1 = hero.remove("슈퍼맨")
print(hero, h1)
#remove는 삭제하여도 요소를 반환하지 않지만
h2 = hero.pop(1)
print(hero, h2) 
#pop은 삭제하면 요소를 반환한다.