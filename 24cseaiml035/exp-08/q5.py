def prime(a):
    for i in range(2,a):
        if a%i==0:
            return"not"
        return""
    a=int(input("enter a number:"))
    print(f"{a} is {prime (a)}a prime number")