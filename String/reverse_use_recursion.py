# How can a given string be reversed using recursion? (solution)


def reverse(string):
	if len(string) == 0:
		return 
	
	temp = string[0]
	reverse(string[1:])
	print(temp, end='')


strin = "reverse"
reverse(strin)

