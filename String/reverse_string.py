# How do you reverse a given string in place? (solution)

string = "ravikant"
reverse_string = string[::-1]
print(reverse_string)


# using slicing operator
def reverse_string(string):
    return string[::-1]
print(reverse_string("hello engineers"))



def reverse_string(string):
    new_string = ""
    for i in range(len(string)-1,-1,-1):
        new_string += string[i]
    return new_string
print(reverse_string("ravi"))

