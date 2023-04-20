import time
import matplotlib.pyplot as plt
from merge_sort import merge_sort
from insertion_sort import insertion_sort

sizes = [1000,2000,3000,4000,5000,6000,7000,8000]
insertion_sort_times_best=[]
merge_sort_times_best=[]
insertion_sort_times_worst=[]
merge_sort_times_worst=[]

for n in sizes:
    arr_best = [i for i in range(n)]
    arr_worst = [i for i in range(n, 0, -1)]
    
    start_time = time.time()
    insertion_sort(arr_best)
    end_time = time.time()
    insertion_sort_times_best.append(end_time - start_time)
    
    start_time = time.time()
    merge_sort(arr_best, 0, len(arr_best)-1)
    end_time = time.time()
    merge_sort_times_best.append(end_time - start_time)

    start_time = time.time()
    insertion_sort(arr_worst)
    end_time = time.time()
    insertion_sort_times_worst.append(end_time - start_time)
    
    start_time = time.time()
    merge_sort(arr_worst, 0, len(arr_best)-1)
    end_time = time.time()
    merge_sort_times_worst.append(end_time - start_time)


plt.plot(sizes, merge_sort_times_best, 'blue', label="Merge sort (best)")
plt.plot(sizes, insertion_sort_times_best,'green', label="Insertion sort (best)")
plt.xlabel("Input size")
plt.ylabel("Execution time (seconds)")
plt.title("Best Cases")
plt.legend()
plt.show()

plt.plot(sizes, merge_sort_times_worst, 'red', label="Merge sort (worst)")
plt.plot(sizes, insertion_sort_times_worst,'orange', label="Insertion sort (worst)")
plt.xlabel("Input size")
plt.ylabel("Execution time (seconds)")
plt.title("Worst Cases")
plt.legend()
plt.show()

plt.plot(sizes, merge_sort_times_worst, 'red', label="Merge sort (worst)")
plt.xlabel("Input size")
plt.ylabel("Execution time (seconds)")
plt.title("Merge Sort All cases")
plt.legend()
plt.show()

