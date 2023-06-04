def counting_sort(arr):
    # Find the range of input elements
    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val + 1

    # Initialize count array and output array
    count = [0] * range_val
    output = [0] * len(arr)

    # Count the occurrences of each element
    for num in arr:
        count[num - min_val] += 1

    # Calculate the cumulative sum of count array
    for i in range(1, range_val):
        count[i] += count[i - 1]

    # Place the elements in the output array based on their count
    for num in reversed(arr):
        index = count[num - min_val] - 1
        output[index] = num
        count[num - min_val] -= 1

    return output

arr = [4, 2, 5, 3, 1, 4, 6]
sorted_arr = counting_sort(arr)

print("Sorted array:", sorted_arr)