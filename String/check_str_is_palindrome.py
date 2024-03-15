# How do you check if a given string is a palindrome? (solution)
##Dn 

def is_palindrome(string):
    if (string == string[::-1]):
        return "  Palindrome"
    else:
        return "Not Palindrome "
palindrome_string = "madam"
print(is_palindrome(palindrome_string))


# using for loop 
string  = "radar"
rever_string  = ""

for i in string:
    rever_string = i+rever_string
print("Reversed string : ",rever_string)
if(string==rever_string):
    print("This string is Palindrome")
else:
    print("This string is not palindrome")