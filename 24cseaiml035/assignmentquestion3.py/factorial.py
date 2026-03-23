x=int(input("enter a number:"))
factorial=1
if x<0:
    print("it is a negetive number")
elif x==0:
    print("the factorial of ",x,"is:",factorial)
else:
    for i in range(1,x+1):
        factorial=factorial*i
        print("the factorial of x",x,"is:",factorial)