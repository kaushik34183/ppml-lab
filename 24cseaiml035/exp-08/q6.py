def rev(st):
    if st == "":
        return ""
    else:
        return rev(st[1:]) + st[0]

n = input("enter a string:")
print(f"{n} reverse is: {rev(n)}")
