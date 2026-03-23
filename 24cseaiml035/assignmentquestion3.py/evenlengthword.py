x=input("enter a string:")
y=""
for c in x:
    if c!="":
        y=y+c
    else:
        if len(y)%2==0:
            print(y)
        y=""
if len(y)%2==0:
    print(y)