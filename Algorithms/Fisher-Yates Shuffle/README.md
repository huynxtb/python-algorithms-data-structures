# Fisher-Yates Shuffle

## Introduction
The Fisher-Yates Shuffle, also known as the Knuth Shuffle, is an efficient algorithm for generating a random permutation of a finite sequence. It ensures that every possible permutation of the sequence is equally likely, making it ideal for applications requiring fair randomization, such as card games, statistical sampling, or cryptographic key generation.

## Usage
Here is an example of how to use the `fisher_yates_shuffle` function:

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


## Detailed Explanation
The algorithm works by iterating over the list from the last element to the second element. In each iteration, it selects a random index from the unsorted portion of the list (from index 0 to the current index) and swaps the current element with the element at the randomly selected index. This process continues until the entire list is shuffled. The use of the random index ensures that all permutations are equally probable.

## Complexity Analysis
- **Time Complexity:** O(n), where n is the number of elements in the list. Each element is processed exactly once.
- **Space Complexity:** O(1), as the shuffling is done in-place and no additional data structures are used.