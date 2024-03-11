# How are duplicates removed from a given array? (solution)



original_list = [1,2,2,3,3,4,4,5,5] 
unique_list = [] 
for item in original_list: 
    if item not in unique_list: 
        unique_list.append(item) 
print(unique_list)
    