def merge_sort(arr):
    """
    Perform a merge sort on the input list and return a new sorted list.

    This function does not mutate the input list; instead it returns a sorted copy.

    Args:
        arr (list of int): The list of integers to sort.

    Returns:
        list of int: A new sorted list containing the elements of the input list.
    """
    # Base case: if the list is empty or has one element, it is already sorted
    if len(arr) <= 1:
        return arr.copy()

    # Divide step: split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive conquer step: sort each half
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge step: merge the two sorted halves into a single sorted list
    sorted_arr = []
    i = j = 0

    # Continue merging until one half is exhausted
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] <= sorted_right[j]:
            sorted_arr.append(sorted_left[i])
            i += 1
        else:
            sorted_arr.append(sorted_right[j])
            j += 1

    # Append any remaining elements from the left half
    while i < len(sorted_left):
        sorted_arr.append(sorted_left[i])
        i += 1

    # Append any remaining elements from the right half
    while j < len(sorted_right):
        sorted_arr.append(sorted_right[j])
        j += 1

    return sorted_arr
