# How do you find the largest and smallest number in an unsorted integer array? (solution)
arr = [15,30,43,60,72,90]
max_num = arr[-1]
min_num = arr[0]

for num in arr:
    if num > max_num:
        max_num = num
    if min_num > num:
        min_num = num
print("Smallest number is :",min_num,"\nLargest number is :",max_num)
