
from algorithms.selection_sort import selection_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.quick_sort import quick_sort
from algorithms.merge_sort import merge_sort


# Test arrays
selection_sort_numbers = [5, 3, 8, 2, 1]

bubble_sort_numbers = [5, 3, 8, 2, 1]

quick_sort_numbers = [5, 3, 8, 2, 1]

merge_sort_numbers = [8, 3, 5, 1, 9, 2, 7, 4]


# Selection Sort
print("\n========== SELECTION SORT ==========")

print("Original Array:", selection_sort_numbers)

sorted_numbers, comparisons, swaps = selection_sort(selection_sort_numbers)

print("Sorted Array:", sorted_numbers)
print("Comparisons:", comparisons)
print("Swaps:", swaps)


# Bubble Sort
print("\n========== BUBBLE SORT ==========")

print("Original Array:", bubble_sort_numbers)

sorted_numbers, comparisons, swaps = bubble_sort(bubble_sort_numbers)

print("Sorted Array:", sorted_numbers)
print("Comparisons:", comparisons)
print("Swaps:", swaps)


# Quick Sort
print("\n========== QUICK SORT ==========")

print("Original Array:", quick_sort_numbers)

sorted_numbers, comparisons, swaps = quick_sort(quick_sort_numbers)

print("Sorted Array:", sorted_numbers)
print("Comparisons:", comparisons)
print("Swaps:", swaps)


# Merge Sort
print("\n========== MERGE SORT ==========")

print("Original Array:", merge_sort_numbers)

sorted_numbers, comparisons = merge_sort(merge_sort_numbers)

print("Sorted Array:", sorted_numbers)
print("Comparisons:", comparisons)
print("Swaps: Not applicable (uses merging)")
