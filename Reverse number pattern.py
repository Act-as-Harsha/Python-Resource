n=int(input("enter the number of rows: "))

for i in range(0,n):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()