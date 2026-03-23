def vowel(s):
    count=0
    for i in s:
        if i in['a','e','i','o','u','A','E','I','O','U']:
            COUNT+=1
            return count
        n=input("enter a string:")
        print(f"{n}contains{vowel(s)}vowels")