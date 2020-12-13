total_charge = 0
def menu():
    print()
    print("시스템 메뉴\n 1. 주문 \n 2.메뉴 추가\n 3.메뉴 삭제\n 4.재고 확인\n 5.재고 추가\n 0.종료\n")

def plus_menu(items, price, num):
    print("현재메뉴 : ", items)
    a = input("추가하실 메뉴 : ")
    if a in items:
        print("존재하는 메뉴 입니다.")
        return
    b = int(input("가격 : "))
    items.append(a)
    price.append(b)
    num.append(10)

def remove_menu(items, order_list, price, num):
    print("현재메뉴 : ", items)
    
    menu_delete = input("삭제하실 메뉴 : ")
    if menu_delete not in items:
        print("존재하지 않는 메뉴입니다.")  
        return 
    
    order_list.pop(items.index(menu_delete))
    price.pop(items.index(menu_delete))
    items.pop(items.index(menu_delete))
    num.pop(items.index(menu_delete))

    print(menu_delete, "을/를 삭제합니다.")

def order_menu(items, price):
    print("주문하실 메뉴는 다음과 같습니다.")
    for i in range(len(items)):
        print(str(i+1)+ ".", items[i], price[i], "원")
    print("0. 주문종료")

def order(items,order_list,price, num):
    global total_charge
    while True:
        menu = int(input("주문하실 메뉴는? : "))
        if menu == 0:
            break
        elif num[menu-1] == 0:
            print("주문하시려는 메뉴의 재고가 없습니다.")
            return 
        else:
            order_list[menu-1]=order_list[menu-1]+1
            total_charge += price[menu-1]
            num[menu-1]=num[menu-1] - 1
    return False 

def result(items,order_list):
    global total_charge
    
    for i in range(len(order_list)):
        if (order_list[i-1]!=0):
            print(items[i-1], ":", order_list[i-1], "잔", end=" ")
    coffeenum = 0
    for i in range(len(order_list)):
        coffeenum += order_list[i-1]

    print("총 ", coffeenum, "잔 입니다.")      
    print("총 금액은 ", total_charge, "입니다.")
    print("감사합니다.")

def check(items, num):
    if len(items) == 0:
        print ("메뉴가 존재하지 않습니다.")
    for i in range(len(items)):
        print(items[i-1], ":", num[i-1], "개")

def checkplus(items, num):
    if len(items) == 0:
        print ("메뉴가 존재하지 않습니다.")
    for i in range(len(items)):
        print(str(items[i-1])+"의 추가 개수 : ", end="")
        mynum= int(input())
        num[i-1]+=mynum