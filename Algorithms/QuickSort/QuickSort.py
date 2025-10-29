def quick_sort(arr):
    """Sorts the list arr in place using the QuickSort algorithm with Lomuto partition scheme."""
    def lomuto_partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = lomuto_partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    if arr:
        quick_sort_recursive(0, len(arr) - 1)
