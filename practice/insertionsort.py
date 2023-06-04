import random


def insertion_sort(arr):
    for i in range (1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
        
# Generate a list of 100 random numbers between 1 and 100
random_numbers = random.sample(range(1, 101), 100)

print("Before sorting:", random_numbers)

# Call the insertion sort function
insertion_sort(random_numbers)

print("After sorting:", random_numbers)