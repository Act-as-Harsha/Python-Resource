a=int(input("enter the number: "))

flag=False

if a==1:
    print(f"{a} is not a prime number")
elif a>1:
    for i in range(2,a):
        if(a%i)==0:
            flag=True
            break
if flag:
    print(f"{a} is not a prime")
else:
    print(f"{a} is a prime")
    


