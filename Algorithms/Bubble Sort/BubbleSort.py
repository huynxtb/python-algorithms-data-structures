def bubble_sort(arr):
    """
    Sorts a list of comparable elements in ascending order using the Bubble Sort algorithm.

    This function modifies the input list in-place.

    Args:
        arr (list): The list of elements to be sorted. Elements must be comparable.

    Returns:
        None: The list is sorted in-place.
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place, so we don't need to check them
        swapped = False
        for j in range(n - 1 - i):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then the array is sorted
        if not swapped:
            break
