def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap root (max element) with last element
        heapify(arr, i, 0)  # Heapify the reduced heap

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap root (largest) with its child if necessary
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)  # Recursively heapify the affected subtree
        
# Driver Code
arr = [5, 2, 3, 1, 4]
n = len(arr)
heap_sort(arr)
print("sorted array:", arr)