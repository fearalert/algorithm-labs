import random

def quick_sort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)

def partition(A,p,r):
    pivot = A[r]
    i = p-1
    
    for j in range(p, r):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
    
    
# Input a list of 10 integers
numbers = [1,4,5,62,45,67,32,42,10,3]

print("Before sorting:", numbers)

# Call the quick sort function
quick_sort(numbers, 0, len(numbers) - 1)

print("After sorting:", numbers)


## Randomized Quick Sort
import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

arr = [9, 5, 7, 3, 1, 8, 6]
quick_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)
