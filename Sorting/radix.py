# How is a radix sort algorithm implemented? (solution)
#Radix Sort using python
def countingSortAlgo(arr, position):
    n = len(arr)
    result = [0] * n
    count = [0] * 10  # Calculating the count of elements in the array arr
    for j in range(0, n):
        element = arr[j] // position
        count[element % 10] += 1  # Calculating the cumulative count
    for j in range(1, 10):
        count[j] += count[j - 1]  # Sorting the elements
    i = n - 1
    while i >= 0:
        element = arr[i] // position
        result[count[element % 10] - 1] = arr[i]
        count[element % 10] -= 1
        i -= 1
    for j in range(0, n):
        arr[j] = result[j]


def radixSortAlgo(arr):  # Acquiring the largest element in the array
    maximum = max(arr)  # Using counting sort to sort digit by digit
    position = 1
    while maximum // position > 0:
        countingSortAlgo(arr, position)
        position *= 10


input = [162, 623, 835, 415, 248]
radixSortAlgo(input)
print(input)