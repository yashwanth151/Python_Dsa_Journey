
def binary_search(a, target):
    start=0
    end= len(a) - 1
    while start<=end:
        mid= start + (end-start)//2
        if target==a[mid]:
            return True
        elif target>a[mid]:
            start = mid+1
        else:
            end = mid - 1
    return False

arr = [2, 3, 4, 5, 7, 8, 9, 21, 32, 45, 65]
print(binary_search(arr, 76))


