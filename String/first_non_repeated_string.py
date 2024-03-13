# How do you print the first non-repeated character from a string? (solution)
# Python program to print the first non-repeating character

string = "ravi ravi kant"
index = -1
fnc = ""

if len(string) == 0 :
    print("EMTPY STRING")

for i in string:
	if string.count(i) == 1:
		fnc += i
		break
	else:
		index += 1
if index == len(string)-1 :
	print("All characters are repeating ")
else:
	
	print("First non-repeating character is -: ", fnc)
