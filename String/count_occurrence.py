# How do you count the occurrence of a given character in a string? (solution)
test_str = "ravi kant patel"
count = 0

for i in test_str:
	if i == 'a':
		count = count + 1
print("Count of occurrence : "
	+ str(count))
