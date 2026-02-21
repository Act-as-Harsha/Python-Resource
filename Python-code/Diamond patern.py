def pyramid(row):
    for i in range(row):
        print(" " * (row - i - 1) + "* " * (i + 1))
    for j in range(row - 1, 0, -1):
        print(" " * (row - j) + "* " * j)

rows = int(input("Enter number of rows: "))
pyramid(rows)
