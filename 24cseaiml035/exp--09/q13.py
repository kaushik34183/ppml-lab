numbers=[1,2,3,4,5,6,7,8,9,16]
even_numbers=list(filter(lambda n:numbers%1==0,numbers))
print(even_numbers)
