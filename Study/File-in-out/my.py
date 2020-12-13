import coffee
import codecs
order_list=[]
items = []
price = []
num = []

infile = codecs.open("goocoffee.txt", "r", "utf-8")

for line in infile.readlines():
    line = line.strip()
    parts = line.split(",")
    order_list.append(0)
    items.append(parts[0])
    price.append(parts[1])
    num.append(10)
infile.close() 
# for i in range (len(items)):
#     num.append(5)

while(True):
    coffee.menu()
    
    number = int(input("메뉴를 선택하시오 : "))
    if (number == 1):
        while True:
            coffee.order_menu(items, price)
            if (coffee.order(items, price, order_list, num)==False):
                coffee.result(items, order_list)
                break
    elif (number == 2):
        coffee.plus_menu(items, price, num)
    elif (number ==3):
        coffee.remove_menu(items, order_list, price, num)
    elif (number== 4):
        coffee.check(items, num)
    elif (number== 5):    
        coffee.checkplus(items, num)
    elif (number ==0):
        outfile = codecs.open("goocoffee.txt", "w", "utf-8")
        for i in range(len(items)):
            outfile.write(items[i]+",")
            outfile.write(str(price[i]) + "\n")
        outfile.close()
        print("종료합니다.")
        break