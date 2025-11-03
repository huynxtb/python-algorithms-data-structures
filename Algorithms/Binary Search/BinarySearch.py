def binary_search(arr, target):
    """
    Perform an iterative binary search on a sorted list to find the target value.

    Parameters:
    arr (List[int]): A sorted list of integers.
    target (int): The integer value to search for in the list.

    Returns:
    int: The index of the target in the list if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Find the middle index to avoid overflow

        # Check if the target is present at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target is not found in the list
    return -1
