p=float(input("enter principal amount"))
t=float(input("enter time"))
r=float(input("enter rate of intrest"))
n=int(input( "Number of times interest is compounded per year"))
si=p*t*r/100
a=p(1+r/n)^(n*t)
print("simple intrest:",si)
print("compound intrest intrest:",a)

