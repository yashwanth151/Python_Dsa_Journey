def merge_sort(arr):
    n = len(arr)
    # Start with subarrays of size 1 and double the size with each iteration
    size = 1
    while size < n:
        # Iterate over the array and merge pairs of subarrays of the current size
        for start in range(0, n, 2 * size):
            mid = min(n, start + size)
            end = min(start + 2 * size, n)
            merge(arr, start, mid, end)
        # Double the size for the next iteration
        size *= 2
    return arr

def merge(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    i = j = 0
    k = start

    # Merge the two subarrays into the original array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy any remaining elements from left or right subarrays
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

A = [4,5,78,2,9,2,4,6,902,5,9,8,3,23]
print(merge_sort(A))