from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
readFile = askopenfilename()
if( readFile != None):
    infile = open(readFile, "r")

for line in infile:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word);

print(word_list[0])
print(word_list[1])
infile.close() 
    

# order_list=[0,0,0]
# items=["아메리카노","라떼","핫초코"]
# price=[3000,3500,4000]

# select = 1
# while True:
#     coffee.menu()
#     select = int(input("메뉴를 선택하세요 : "))
#     if select == 1:
#         coffee.order_menu(items,price)
#         coffee.order(items,price,order_list)
#         coffee.result(items,order_list)
#     if select == 0:
#         print("종료합니다.")
#         break

