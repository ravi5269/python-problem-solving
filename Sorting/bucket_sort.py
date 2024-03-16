def insertion_sort(arr):
    # Insertion sort function for sorting individual buckets
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort(arr):
    # Determine the number of buckets to use
    num_buckets = len(arr)

    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets
    for num in arr:
        bucket_index = int(num * num_buckets)
        buckets[bucket_index].append(num)

    # Sort individual buckets
    for bucket in buckets:
        insertion_sort(bucket)

    # Concatenate sorted buckets to produce the final sorted array
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# Example usage
arr = [0.79,0.13,0.64,0.39]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)
