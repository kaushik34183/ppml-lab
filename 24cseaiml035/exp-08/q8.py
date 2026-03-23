def largest(a,b,c):
    return a if (a) >= b  and a>=c else b if (b)>=c else c
a=int (input("enter 1st value:"))
b=int(input("enter 2nd value:"))
c=int(input("enter 3rd value"))
print("largest among three number is:",largest(a,b,c))