s = [[1,2,3], [4,5,6], [7,8,9]]

rows= len(s)
cols = len(s[0])    

for i in range (rows):
    for j in range (cols):
        print(s[i][j], end=",")
    print()