import random
from binary_search import binary_search
from linear_search import linear_search
from measure_time import measure_time

def generate_input(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Generate inputs and measure execution time for each algorithm
sizes = range(10000, 110000, 10000)
linear_times_best = []
linear_times_worst = []
binary_times_best = []
binary_times_worst = []

for size in sizes:
    # Generate input and value to search for
    arr = generate_input(size)
    x = random.choice(arr)
    # Measure execution time for linear search (best case)
    linear_times_best.append(measure_time(linear_search, arr, arr[0]))

    # Measure execution time for linear search (worst case)
    linear_times_worst.append(measure_time(linear_search, arr, -1))

    # Sort the input for binary search
    arr.sort()

    # Measure execution time for binary search (best case)
    binary_times_best.append(measure_time(binary_search, arr, arr[0]))

    # Measure execution time for binary search (worst case)
    binary_times_worst.append(measure_time(binary_search, arr, -1))

# Plot the results
import matplotlib.pyplot as plt

plt.plot(sizes, linear_times_best,'green', label="Linear Search (Best Case)")
plt.plot(sizes, linear_times_worst,'red', label="Linear Search (Worst Case)")
plt.plot(sizes, binary_times_best,'yellow', label="Binary Search (Best Case)")
plt.plot(sizes, binary_times_worst,'orange', label="Binary Search (Worst Case)")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Linear Search vs Binary Search")
plt.legend()
plt.show()
