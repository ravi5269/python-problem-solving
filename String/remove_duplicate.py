# how to remove the duplicate character from String? (solution)

string = "hello django "

p=""
for char in string:
    if char not in p:
        p=p+char
print("Orignal String :",string)
print("After remove duplicate string  :",p)
