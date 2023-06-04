def binary_search(arr, key, left, right):
    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            binary_search(arr, key, mid+1, right)
        else:
            binary_search(arr, key, left, mid-1)
    
    return -1

arr = [2, 4, 6, 8, 10]
key = 6
result = binary_search(arr, key, 0, len(arr) - 1)
print("Element", key, "found at index:", result)