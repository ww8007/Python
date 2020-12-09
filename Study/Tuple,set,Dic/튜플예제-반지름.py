import math 

def get(my):
    rad = 2 * math.pi * my
    sol = math.pi * r **2
    return (rad, sol)
r = int(input("반지름 입력 : "))

ans = get(r)

print(ans)