# How do you check if a given string is a palindrome? (solution)

a = "madam"
b = a[-1::-1]
if(a==b):
    print("Palindrome String")
else:
    print("Not Palindrome")