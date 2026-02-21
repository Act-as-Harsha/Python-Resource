n=int(input("Enter the number of rows: "))

b = 0

for i in range(n, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=" ")
    print()
