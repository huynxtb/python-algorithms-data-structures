def selection_sort(arr: list) -> None:
    """
    Sorts a list of comparable elements in-place using the Selection Sort algorithm.

    Selection Sort works by repeatedly finding the minimum element from the unsorted
    part of the list and putting it at the beginning of the unsorted part.

    Args:
        arr: The list of comparable elements to be sorted. The list is modified in-place.

    Returns:
        None
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element of the unsorted part
        # Only swap if the minimum element is not already in its correct position
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
