"""
Pivot Points -- Building and Benchmarking Quicksort
Chapter 4: Divide and Conquer
"""

import random
import time


# ---------------------------------------------------------------------------
# PART 1: Divide & Conquer warm-ups
# ---------------------------------------------------------------------------

def recursive_sum(arr):
    if not arr:
        return 0

    return arr[0] + recursive_sum(arr[1:])


def recursive_count(arr):
    if not arr:
        return 0

    return 1 + recursive_count(arr[1:])


def recursive_max(arr):
    if not arr:
        raise ValueError("recursive_max() requires a non-empty list")

    if len(arr) == 1:
        return arr[0]

    sub_max = recursive_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


def binary_search_recursive(arr, target):
    def helper(low, high):
        if low > high:
            return -1

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            return helper(mid + 1, high)

        return helper(low, mid - 1)

    return helper(0, len(arr) - 1)


# ---------------------------------------------------------------------------
# PART 2: Quicksort
# ---------------------------------------------------------------------------

def quicksort(array, pivot_strategy="first"):
    if len(array) < 2:
        return list(array)

    if pivot_strategy == "first":
        pivot_index = 0
    elif pivot_strategy == "random":
        pivot_index = random.randrange(len(array))
    elif pivot_strategy == "middle":
        pivot_index = len(array) // 2
    else:
        raise ValueError(
            f"Unknown pivot strategy: {pivot_strategy!r}"
        )

    pivot = array[pivot_index]

    rest = (
        array[:pivot_index]
        + array[pivot_index + 1:]
    )

    less = [value for value in rest if value < pivot]
    greater_or_equal = [
        value for value in rest if value >= pivot
    ]

    return (
        quicksort(less, pivot_strategy)
        + [pivot]
        + quicksort(greater_or_equal, pivot_strategy)
    )


# ---------------------------------------------------------------------------
# PART 3: Empirical worst-case vs. average-case investigation
# ---------------------------------------------------------------------------

def measure_time(arr, pivot_strategy):
    start = time.perf_counter()

    try:
        result = quicksort(list(arr), pivot_strategy)
    except RecursionError:
        return None

    elapsed = time.perf_counter() - start

    # Confirm that Quicksort produced the correct result.
    if result != sorted(arr):
        raise RuntimeError("Quicksort produced an incorrect result")

    return elapsed


def run_benchmark(unsorted_list, sorted_list, reverse_sorted_list):
    input_shapes = {
        "unsorted": unsorted_list,
        "sorted": sorted_list,
        "reverse sorted": reverse_sorted_list,
    }

    pivot_strategies = ["first", "random"]

    print(f"{'shape':<18}{'strategy':<12}{'result':<18}")
    print("-" * 48)

    for shape_name, data in input_shapes.items():
        for strategy in pivot_strategies:
            elapsed = measure_time(data, strategy)

            if elapsed is None:
                result_text = "RecursionError"
            else:
                result_text = f"{elapsed:.6f} s"

            print(
                f"{shape_name:<18}"
                f"{strategy:<12}"
                f"{result_text:<18}"
            )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    # A fixed seed makes the experiment reproducible.
    random.seed(42)

    sample_numbers = [
        4, 7, 1, 9, 3, 8, 2, 6, 5, 10, 0, -3
    ]

    print("Part 1: Divide & Conquer warm-ups")
    print("recursive_sum:", recursive_sum(sample_numbers))
    print("recursive_count:", recursive_count(sample_numbers))
    print("recursive_max:", recursive_max(sample_numbers))

    sorted_sample = sorted(sample_numbers)

    print(
        "binary_search_recursive (target=8):",
        binary_search_recursive(sorted_sample, 8),
    )
    print(
        "binary_search_recursive (target=99):",
        binary_search_recursive(sorted_sample, 99),
    )

    print("\nPart 2: Quicksort")
    print("first pivot:", quicksort(sample_numbers, "first"))
    print("random pivot:", quicksort(sample_numbers, "random"))
    print("middle pivot:", quicksort(sample_numbers, "middle"))

    print("\nPart 3: Benchmark")

    n = 1000

    # Each input contains the same values but in a different order.
    sorted_list = list(range(n))
    reverse_sorted_list = list(reversed(sorted_list))
    unsorted_list = sorted_list.copy()
    random.shuffle(unsorted_list)

    run_benchmark(
        unsorted_list,
        sorted_list,
        reverse_sorted_list,
    )


if __name__ == "__main__":
