import time

def measure_time(algorithm, arr, x):
    start_time = time.time()
    algorithm(arr, x)
    end_time = time.time()
    return end_time - start_time