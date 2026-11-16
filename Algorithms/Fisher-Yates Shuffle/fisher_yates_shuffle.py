import random

def fisher_yates_shuffle(arr: list) -> None:
    """
    Randomly reorders the elements of the input list in-place using the Fisher-Yates Shuffle algorithm.

    Parameters:
    arr (list): A mutable list of elements to be shuffled.

    This function modifies the input list directly and does not return any value.

    Example:
    >>> my_list = [1, 2, 3, 4, 5]
    >>> fisher_yates_shuffle(my_list)
    >>> print(my_list)
    [3, 1, 4, 5, 2]  # The output will vary as it is randomized.
    """
    n = len(arr)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]