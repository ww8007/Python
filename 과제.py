items = {'콜라' : {'price':1000, 'can' : 'x', 'left':5}, '사이다' : {'price':1000, 'can' : 'x','left':5}, '식혜' : {'price':1000, 'can' : 'x','left':5},
'환타' : {'price':800, 'can' : 'x','left':5}, '밀키스' : {'price':800, 'can' : 'x','left':5}, '제로콜라' : {'price':800, 'can' : 'x','left':5}, '칸타타' : {'price':600, 'can' : 'x','left':5}, '레쓰비' : {'price':600, 'can' : 'x','left':5}, '조지아' : {'price':600, 'can' : 'o','left':5}}

total_money = 0

def input_money():
    global total_money
    total_money = int(input("현금을 투입하세요 : "))
    for i in items.keys():
        if (items[i]['price'] <= total_money):
            items[i]['can'] = 'o'
        else:
            items[i]['can']='x'

def menu():
    global total_money
    j=0
    for i in items.keys():
        
        if j % 3 ==0:
            print('\n')
        print (i, end=" ")
        print(items[i]['can'], end=" ")
        print(items[i]['price'],'원',end=" ")
        print(items[i]['left'], '개',end=" ")
        j+=1
        if (j % 9 == 0):
            print("\n투입금액 : ", total_money)

def purchase():
    global total_money
    order = input("음료수를 선택하세요 : ")
    if items[order]['can'] == 'o':
        if items[order]['price'] <= total_money:
            if items[order]['left'] != 0:
                items[order]['left'] -= 1;
                if items[order]['left'] == 0:
                    items[order]['can'] == 'x'
                print(order+'를 주문완료했습니다.')
                total_money -= items[order]['price']
                print('잔액 : ', total_money, end=" ")
                reorder = input('구매를 계속하시겠습니까?(yes/no): ')
                if (reorder == 'yes'):
                    return 1
                elif  reorder == 'no':
                    return 0
            else:
                print('재고부족')
        else:
            print('금액부족')
    else:
        print('주문 할 수 없습니다.')

            
print('자판기')
menu()
input_money()
menu()
yes_or_no=purchase()
if yes_or_no == 1:
    menu()
    purchase()



