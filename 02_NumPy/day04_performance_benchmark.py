import numpy as np
import time
import math
import sys # sys module lets python interact with the operating system.

print("\n===== NumPy vs Python Lists Benchmark =====")

size = 1_000_000
python_list = list(range(size))
numpy_array = np.arange(size)

# Python lists store references to individual Python objects,
# while NumPy arrays store values in one contiguous block of memory.
# This makes NumPy much more memory-efficient and faster for numerical computations.

# Benchmark Addition
print('\n==== Addition Time ====')
start = time.perf_counter()
python_addition = [x + 5 for x in python_list]
end = time.perf_counter()

python_addition_time = end - start
print(f'Python List: {python_addition_time:.6f} seconds' )

start = time.perf_counter()
numpy_addition = numpy_array + 5
end = time.perf_counter()

numpy_addition_time = end - start
print(f'Numpy Array: {numpy_addition_time:.6f} seconds')

# Benchmark Multiplication
print('\n==== Multiplication Time ====')
start = time.perf_counter()
python_mult = [x * 5 for x in python_list]
end = time.perf_counter()

python_mult_time = end - start
print(f'Python List: {python_mult_time:.6f} seconds')

start = time.perf_counter()
numpy_mult = numpy_array * 5
end = time.perf_counter()

numpy_mult_time = end - start
print(f'Numpy Array: {numpy_mult_time:.6f} seconds')

# Benchmark Square Root
print('\n==== Square Root Time ====')
start = time.perf_counter()
python_sqr = [math.sqrt(x) for x in python_list]
end = time.perf_counter()

python_sqr_time = end - start
print(f'Python List: {python_sqr_time:.6f} seconds')

start = time.perf_counter()
numpy_sqr = np.sqrt(numpy_array)
end = time.perf_counter()

numpy_sqr_time = end - start
print(f'Numpy Array: {numpy_sqr_time:.6f} seconds')

# Benchmark Sum
print('\n==== Sum Time ====')
start = time.perf_counter()
python_sum = sum(python_list)
end = time.perf_counter()

python_sum_time = end - start
print(f'Python List: {python_sum_time:.6f} seconds')

start = time.perf_counter()
numpy_sum = np.sum(numpy_array)
end = time.perf_counter()

numpy_sum_time = end - start
print(f'Numpy Array: {numpy_sum_time:.6f} seconds')

# Benchmark Mean
print('\n==== Mean Time ====')
start = time.perf_counter()
python_mean = sum(python_list) / len(python_list)
end = time.perf_counter()

python_mean_time = end - start
print(f'Python List: {python_mean_time:.6f} seconds')

start = time.perf_counter()
numpy_mean = np.mean(numpy_array)
end = time.perf_counter()

numpy_mean_time = end - start
print(f'Numpy Array: {numpy_mean_time:.6f} seconds')

# Memory Usage
print('\n==== Memory Usage ====')
python_memory = sys.getsizeof(python_list)
numpy_memory = numpy_array.nbytes

print(f'Python List: {python_memory} bytes')
print(f'Numpy Array: {numpy_memory} bytes')


# Speed Comparison
print("\n===== Speed Comparison =====")
print(f"Addition       : {python_addition_time/ numpy_addition_time:.2f}x faster with NumPy")
print(f"Multiplication : {python_mult_time / numpy_mult_time:.2f}x faster with NumPy")
print(f"Square Root    : {python_sqr_time/ numpy_sqr_time:.2f}x faster with NumPy")
print(f"Sum            : {python_sum_time / numpy_sum_time:.2f}x faster with NumPy")
print(f"Mean           : {python_mean_time / numpy_mean_time:.2f}x faster with NumPy")

print('\n==== Conclusion ====')
print("NumPy performs numerical operations much faster than Python lists.")
print("It uses vectorized operations instead of processing one element at a time.")
print("NumPy is the preferred choice for numerical computing and data analysis.\n")