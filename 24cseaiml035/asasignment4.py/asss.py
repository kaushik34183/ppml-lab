#wap to print 2nd largest and 2nd smallest elementin alist of 10 integers without using sort function()
arr=[]
x=int(input("enter number of elements:"))
for i in range(x):
    m=int(input("enter the element:"))
    arr.append(m)
for j in range(len(arr)-1):
    for k in range(len(arr)-j-1):
        if arr[k]>arr[k+1]:
            arr[k],arr[k+1]=arr[k+1],arr[k]
print("the sorted array is:")
print(arr)
second_largest=arr[-2]
second_smallest=arr[1]
print("second largest element is :",second_largest)
print("second smallest element is :",second_smallest)
#wap to create 2 lists 1st list containg 5 integers and 2nd containing 5.print both list 1 element from each list combined at a time.
list1=[1,2,3,4]
list2=["A","B","C","D","E"]
s=[]
for i in range(len(list1)):
    s.append(str(list1[i]))
    s.append(list2[i])
print(s)
#wap to ceeate an integer list of 20 elements increase the odd valued elements by 5.
s=[]
x=int(input("enter the number of elements:"))
for i in range(x):
    if s[i]%2!=0:
        s[i]=s[i]+5
print(s)
#wap to create a function that prints the 1st 15 terms of fibonacci series without using recursion.
def fibonacci(n):
    a=0
    b =1
    print(a,b,end="")
    print(b)
    for i in range(2,n):
        c=a+b
        print(c,end="")
        a=b
        b=c
n=int(input("enter the number of terms u want to print:"))
print("the fibonacci series of first",n,"terms are:")

#wap to create a function that takes list as argument and returns even values of a list .print new list with even values.
def even_len(n):
    s=[]
    for i in n:
        if i%2==0:
            s.append(i)
    return s
x=input("enter the list of elements:")
n=[int(i) for i in x.split(",")],s
s=even_len(n)
print(s)
##wap to calculate factorial of a number using recursion
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
n=int (input("rnter the number:"))
if(n<0):
    print("it is a negetive number")
else:
    print("factorial of ,n,is : ",factorial(n))
          