# How do you remove duplicates from an array in place? (solution)
# using set mathod
test_list = [1,2,3,4,4,5,5]
print(" Original list :",test_list)

test_list = list(set(test_list))
print("Remove duplicate",test_list)


# using dict.fromkeys mathod
original_list = [2, 3, 4, 2, 5, 4, 6, 7]
unique_list = list(dict.fromkeys(original_list)) 
print(unique_list)