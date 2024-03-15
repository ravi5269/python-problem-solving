# How do you check if two strings are anagrams of each other? (solution)

str1 = "ravikant"
str2 = "tkanivar"

if len(str1) != len(str2):
    print("Not Anagrams")
else:
    if sorted(str1) == sorted(str2):
        print("String are Anagrams")
  