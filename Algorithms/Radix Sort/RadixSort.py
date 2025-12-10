def radix_sort(arr):
    """
    Perform LSD Radix Sort on a list of non-negative integers.

    Parameters:
    arr (list of int): A list of non-negative integers to sort.

    Returns:
    list of int: A new list containing the sorted integers.
    """
    if not arr:
        return []

    # Create a copy to avoid modifying the input list
    output = list(arr)

    # Find the maximum number to know the number of digits
    max_num = max(output)

    exp = 1  # Exponent representing the digit position (1, 10, 100, ...)

    # Process counting sort for each digit from LSD to MSD
    while max_num // exp > 0:
        output = _counting_sort_by_digit(output, exp)
        exp *= 10

    return output


def _counting_sort_by_digit(arr, exp):
    """
    A helper function to perform counting sort based on the digit represented by exp.

    Parameters:
    arr (list of int): The list to sort by the specific digit.
    exp (int): The exponent corresponding to the digit position.

    Returns:
    list of int: List sorted by the digit at exp position.
    """
    n = len(arr)
    output = [0] * n  # output array
    count = [0] * 10  # digits 0-9

    # Store count of occurrences in count[]
    for number in arr:
        index = (number // exp) % 10
        count[index] += 1

    # Change count[i] so that it contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    # Iterate in reverse to maintain stability
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output
