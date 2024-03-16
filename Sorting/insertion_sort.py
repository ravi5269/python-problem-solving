# How do you implement an insertion sort algorithm? (solution)
def insertion_sort(arr):
    n = len(arr)

    for i in range(1,n):
        key = arr[i]
        j = i-1

        while j>=0 and key <arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key

arr = [20,10,40,50,30]
insertion_sort(arr)
print("Sorted arry  :",arr)
