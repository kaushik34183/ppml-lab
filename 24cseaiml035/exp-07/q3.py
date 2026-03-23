
paragraph = "A man a plan a canal Panama. This is a test sentence with some palindromes like radar and level."

words = paragraph.split()

word_count = len(words)
print("Number of words:", word_count)

palindrome_count = 0
for word in words:
    
    clean_word = ''.join(c for c in word if c.isalnum()).lower()
    if clean_word == clean_word[::-1] and len(clean_word) > 1:
        palindrome_count += 1
print("Number of palindromes:", palindrome_count)

print("Each word in reverse:")
for word in words:
    reversed_word = word[::-1]
    print(reversed_word)
