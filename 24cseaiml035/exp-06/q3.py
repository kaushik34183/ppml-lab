sentence = input("enter a sentence:")
list1 = sentence.split()
print("\n elements of list1 with index:")
for idx, word in enumerate(list1):
    print(idx, word)

list2 = list(range(1, len(list1) + 1))
list3 = list(zip(list1, list2))
print("\n combined list3 using zip:")
print(list3)
