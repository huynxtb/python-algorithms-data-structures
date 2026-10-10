from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers in-place using the Insertion Sort algorithm.

    Insertion Sort builds the final sorted array one item at a time. It iterates
    through the input, taking each element and inserting it into its correct
    position within the already sorted portion of the array.

    This implementation is stable, meaning that the relative order of equal
    elements is preserved.

    Args:
        arr: The list of integers to be sorted.

    Returns:
        The sorted list (the same list object passed as input, modified in-place).
    """
    n = len(arr)
    # Traverse through 1 to len(arr)
    for i in range(1, n):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr