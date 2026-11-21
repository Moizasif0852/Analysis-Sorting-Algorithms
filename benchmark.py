import time
import csv
import os

from algorithms.selection_sort import selection_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.quick_sort import quick_sort
from algorithms.merge_sort import merge_sort


# Required input cases
test_cases = {
    "Size 5 - Sorted": list(range(1, 6)),
    "Size 5 - Reverse": list(range(5, 0, -1)),
    "Size 100 - Sorted": list(range(1, 101)),
    "Size 100 - Reverse": list(range(100, 0, -1))
}

algorithms = {
    "Selection Sort": selection_sort,
    "Bubble Sort": bubble_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort
}

RUNS = 3
results = []


for case_name, original_array in test_cases.items():

    print(f"\n========== {case_name} ==========")

    for algorithm_name, algorithm in algorithms.items():

        times = []

        # Run the algorithm 3 times
        for _ in range(RUNS):

            arr = original_array.copy()

            start_time = time.perf_counter()

            output = algorithm(arr)

            end_time = time.perf_counter()

            times.append(end_time - start_time)

        average_time = sum(times) / RUNS

        # Get comparison and swap counts
        arr = original_array.copy()
        output = algorithm(arr)

        if algorithm_name == "Merge Sort":
            sorted_array, comparisons = output
            swaps = "N/A"
        else:
            sorted_array, comparisons, swaps = output

        # Verify sorting correctness
        assert sorted_array == sorted(original_array)

        average_microseconds = average_time * 1_000_000

        results.append([
            case_name,
            algorithm_name,
            round(average_microseconds, 4),
            comparisons,
            swaps
        ])

        print(
            f"{algorithm_name}: "
            f"{average_microseconds:.4f} microseconds | "
            f"Comparisons: {comparisons} | "
            f"Swaps: {swaps}"
        )


# Save results to CSV
with open("results/results.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Test Case",
        "Algorithm",
        "Average Time (Microseconds)",
        "Comparisons",
        "Swaps"
    ])

    writer.writerows(results)


print("\nBenchmark completed successfully!")
os.makedirs("results", exist_ok=True)
print("Results saved in results.csv")
