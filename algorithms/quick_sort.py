def quick_sort(arr):

    comparisons = 0
    swaps = 0

    def partition(low, high):

        nonlocal comparisons, swaps

        pivot = arr[high]
        i = low - 1

        for j in range(low, high):

            comparisons += 1

            if arr[j] <= pivot:

                i += 1

                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1

        if i + 1 != high:
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            swaps += 1

        return i + 1

    def quick_sort_recursive(low, high):

        if low < high:

            pivot_index = partition(low, high)

            quick_sort_recursive(low, pivot_index - 1)
            quick_sort_recursive(pivot_index + 1, high)

    quick_sort_recursive(0, len(arr) - 1)

    return arr, comparisons, swaps
