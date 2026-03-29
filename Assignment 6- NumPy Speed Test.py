# ==========================================
# Assignment 6: NumPy Speed Test
# Date: 20/02/2026
# ==========================================

import numpy as np
import time

# Number of elements
N = 1_000_000


# -------------------------------
# Utility Function
# -------------------------------

def measure_time(func):
    """Measure execution time of a function"""
    start = time.perf_counter()
    result = func()
    end = time.perf_counter()
    return result, end - start


# -------------------------------
# Test 1: Creation
# -------------------------------

py_list, list_create_time = measure_time(lambda: list(range(N)))
np_array, np_create_time = measure_time(lambda: np.arange(N))


# -------------------------------
# Test 2: Summation
# -------------------------------

_, list_sum_time = measure_time(lambda: sum(py_list))
_, np_sum_time = measure_time(lambda: np.sum(np_array))


# -------------------------------
# Test 3: Multiplication
# -------------------------------

_, list_mul_time = measure_time(lambda: [x * 2 for x in py_list])
_, np_mul_time = measure_time(lambda: np_array * 2)


# -------------------------------
# Display Results
# -------------------------------

def display_results():
    print("=" * 60)
    print(f"{'Operation':<20}{'Python List':>15}{'NumPy':>15}")
    print("=" * 60)

    print(f"{'Creation':<20}{list_create_time:>14.6f}s{np_create_time:>14.6f}s")
    print(f"{'Sum':<20}{list_sum_time:>14.6f}s{np_sum_time:>14.6f}s")
    print(f"{'Multiply x2':<20}{list_mul_time:>14.6f}s{np_mul_time:>14.6f}s")

    print("=" * 60)

    print("\n--- Observations ---")
    print("1. NumPy operations are faster due to vectorized execution.")
    print("2. NumPy arrays are more memory efficient than Python lists.")
    print("3. Performance difference increases with larger datasets.")


# -------------------------------
# Main Function
# -------------------------------

def main():
    print("=== NumPy Speed Test ===\n")
    display_results()


# Entry Point
if __name__ == "__main__":
    main()