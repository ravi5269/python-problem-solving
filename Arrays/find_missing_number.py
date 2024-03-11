# How do you find the missing number in a given integer array of 1 to 100? (solution)
arr = [1,2,3,4,7,8,9,10]
missing_elements = []
for element in range(arr[0], arr[-1]+1):
    if element not in arr:
        missing_elements.append(element)
print(missing_elements)

