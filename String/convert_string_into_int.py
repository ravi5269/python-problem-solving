# How do you convert a given String into int? (solution)


# convert a string into integer 

# from ast import literal_eval

# int_value = literal_eval("1234")
# print(int_value)
# print(type(int_value))

string = "125"
if string.isdigit():
	integer = int(string)
	print(integer) 
else:
	print(f"{string} is not a valid integer.")

