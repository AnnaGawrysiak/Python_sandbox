import numpy as np

def binary_search( val, arr):
    arr = np.sort(arr)

    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            high = mid - 1
        elif arr[mid] < val:
            low = mid + 1
    return -1

value = 8
arr = np.array([4, 6, 8, 7, 9, 10, 11])
print(binary_search(value, arr))