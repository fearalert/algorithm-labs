def bucket_sort(arr):
    # Determine the range of input values
    min_val = min(arr)
    max_val = max(arr)
    num_buckets = len(arr)

    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets based on their value range
    for num in arr:
        index = int((num - min_val) * (num_buckets - 1) / (max_val - min_val))
        buckets[index].append(num)

    # Sort elements within each bucket
    for bucket in buckets:
        bucket.sort()

    # Concatenate the sorted elements from all buckets
    sorted_arr = [num for bucket in buckets for num in bucket]

    return sorted_arr


arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
sorted_arr = bucket_sort(arr)

print("Sorted array:", sorted_arr)
