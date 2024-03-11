# How do you find the duplicate number on a given integer array? (solution)
arr = [1, 2, 3, 4, 4, 5,5]

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]==arr[j]):
            print(arr[j])