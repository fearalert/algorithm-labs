def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count the occurrences of digits at the given exponent
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Calculate the cumulative sum of count array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in the output array based on their count and digit value
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the sorted elements from the output array to the original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # Find the maximum element to determine the number of digits
    max_val = max(arr)

    # Perform counting sort for each digit from least significant to most significant
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)

print("Sorted array:", arr)
