def print_H(row, col):
    return col == 0 or col == 4 or row == 3

def print_A(row, col):
    return (row == 0 and col != 0 and col != 4) or (row == 3) or (col == 0 or col == 4) and row != 0

def print_R(row, col):
    return col == 0 or (row == 0 or row == 3) and col < 4 or (col == 4 and row in [1, 2]) or (row - col == 2)

def print_S(row, col):
    return (row == 0 or row == 3 or row == 6) or (col == 0 and row < 3) or (col == 4 and row > 3)

def print_space():
    return "   "  

letters = [print_H, print_A, print_R, print_S, print_H, print_A]

for row in range(7): 
    for letter_func in letters:
        for col in range(5):  
            if letter_func(row, col):
                print("*", end="")
            else:
                print(" ", end="")
        print(" ", end=" ") 
    print() 
