def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    print("key not found")
    return -1

arr = [2, 4, 6, 8, 10]
key = 8
result = linear_search(arr, key)
print("Element", key, "found at index:", result)