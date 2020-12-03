infile = open("goocoffee.txt", "r+")
import coffee
order_list=[]
items = []
price = []
f=open("goocoffee.txt", "r")

for line in f.readlines():
    line = line.strip()
    parts = line.split(",")
    order_list.append(0)
    items.append(parts[0])
    price.append(int(parts[1]))
infile.close() 

while(True):
    coffee.menu()
    number = int(input("메뉴를 선택하시오 : "))
    if (number == 1):
        while True:
            coffee.order_menu(items, price)
            mynum = int(input("주문하실 메뉴는? : "))
            if (coffee.order(items, price, order_list)==False):
                break
            
        
    elif (number == 2):
        coffee.plus_menu(items, price)
    elif (number ==3):
        coffee.remove_menu(items, order_list, price)
    elif (number ==0):
        outfile = open ("goocoffee.txt", "w")
        for i in range(len(items)):
            outfile.write(items[i]+",")
            outfile.write(str(price[i]) + "\n")
        outfile.close()
        print("종료합니다.")
        break
    