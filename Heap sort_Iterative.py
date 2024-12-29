def heapify(arr, root_index, n):
    current_root_index = root_index

    while True:
        i = current_root_index
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2

        # Finding the index of the largest value among:
        # arr[current_root_index], arr[left_child_index], and arr[right_child_index].
        if left_child_index < n and arr[left_child_index] > arr[i]:
            i = left_child_index
        if right_child_index < n and arr[right_child_index] > arr[i]:
            i = right_child_index

        # The largest among the three considered values will now be the root of the Max-Heap
        # represented by arr[current_root_index ... n - 1].
        if i != current_root_index:
            arr[i], arr[current_root_index] = arr[current_root_index], arr[i]
            current_root_index = i
        else:
            break

def heap_sort(arr):
    n = len(arr)

    # Building a Max-Heap in a bottom-up manner.
    # Heapifying only the indices in range [0, n/2 - 1) because only these indices will have at least one
    # child node in the Max-Heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

    return arr

A=[7,5,1,34,9,33,00,12,3,77,8,90,3,5,99]
print(heap_sort(A))