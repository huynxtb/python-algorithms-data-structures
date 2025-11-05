def counting_sort(arr):
    """
    Sort a list of non-negative integers using the Counting Sort algorithm.

    Args:
        arr (List[int]): The list of non-negative integers to sort.

    Returns:
        List[int]: A new list containing the sorted elements.
    """
    if not arr:
        return []

    # Find the maximum value to determine the range of counts
    max_value = max(arr)

    # Initialize count array with zeros
    count = [0] * (max_value + 1)

    # Count the occurrences of each value in arr
    for num in arr:
        count[num] += 1

    # Construct the sorted array
    sorted_arr = []
    for value, frequency in enumerate(count):
        sorted_arr.extend([value] * frequency)

    return sorted_arr
