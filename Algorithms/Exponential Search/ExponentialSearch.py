def binary_search(arr, left, right, target):
    """
    Helper function: Performs binary search on a subarray.
    
    Args:
        arr: The sorted list to search in.
        left: The left boundary index of the subarray.
        right: The right boundary index of the subarray.
        target: The value to search for.
    
    Returns:
        The index of the target if found, otherwise -1.
    """
    while left <= right:
        # Calculate the middle index to avoid potential overflow
        mid = left + (right - left) // 2

        # Check if the target is at the middle
        if arr[mid] == target:
            return mid
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore the right half
        else:
            right = mid - 1

    # Target was not found in the subarray
    return -1


def exponential_search(arr, target):
    """
    Performs an Exponential Search on a sorted list.

    The algorithm works in two phases:
      1. Find the range where the target may exist by doubling the index
         exponentially (1, 2, 4, 8, 16, ...).
      2. Perform a binary search within that identified range.

    Args:
        arr: A sorted list of comparable elements.
        target: The value to search for in the list.

    Returns:
        The index of the target in the list if found, otherwise -1.
    """
    n = len(arr)

    # Handle the edge case of an empty array
    if n == 0:
        return -1

    # Check if the target is at the very first position
    if arr[0] == target:
        return 0

    # Phase 1: Find the range for binary search.
    # Start with index 1 and keep doubling until we either go out of bounds
    # or find an element greater than or equal to the target.
    index = 1
    while index < n and arr[index] <= target:
        # Double the index to expand the search range exponentially
        index *= 2

    # Phase 2: Perform binary search in the identified range.
    # The range is from (index // 2) to min(index, n - 1).
    # - index // 2 is the last valid position from the previous iteration
    # - min(index, n - 1) ensures we don't go out of bounds
    left_boundary = index // 2
    right_boundary = min(index, n - 1)

    return binary_search(arr, left_boundary, right_boundary, target)
