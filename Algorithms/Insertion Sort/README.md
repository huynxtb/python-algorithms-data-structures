# Insertion Sort

## Introduction

Insertion Sort is a simple, in-place comparison sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, insertion sort provides several advantages:

*   **Simple implementation:** It is easy to implement and understand.
*   **Efficient for small data sets:** It is efficient for small lists or for lists that are already partially sorted.
*   **Stable:** It is a stable sorting algorithm, meaning that the relative order of equal elements is preserved.
*   **In-place:** It sorts the array in-place, requiring only a constant amount of additional memory space.

It is often used as a subroutine in more advanced algorithms, such as Timsort (used in Python) and Introsort.

## Usage


from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers in-place using the Insertion Sort algorithm.

    Args:
        arr: The list of integers to be sorted.

    Returns:
        The sorted list (the same list object passed as input, modified in-place).
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
my_list = [12, 11, 13, 5, 6]
print(f"Original list: {my_list}")
sorted_list = insertion_sort(my_list)
print(f"Sorted list: {sorted_list}")

my_list_2 = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original list: {my_list_2}")
sorted_list_2 = insertion_sort(my_list_2)
print(f"Sorted list: {sorted_list_2}")


## Detailed Explanation

The `insertion_sort` function takes a list of integers `arr` as input and sorts it in-place.

1.  **Initialization:** The algorithm iterates through the list starting from the second element (index 1). The first element (index 0) is considered to be a sorted sublist of size 1.

2.  **Iteration:** For each element `arr[i]` (starting from `i = 1` up to `n-1`):
    *   The current element `arr[i]` is stored in a variable called `key`.
    *   A pointer `j` is initialized to `i - 1`, pointing to the last element of the already sorted sublist.

3.  **Shifting:** The `while` loop compares `key` with the elements in the sorted sublist (`arr[j]`).
    *   If `key` is smaller than `arr[j]`, it means `arr[j]` is not in its correct sorted position relative to `key`. Therefore, `arr[j]` is shifted one position to the right (`arr[j + 1] = arr[j]`).
    *   The pointer `j` is decremented (`j -= 1`) to move to the next element in the sorted sublist.
    *   This process continues as long as `j` is non-negative and `key` is smaller than `arr[j]`.

4.  **Insertion:** Once the `while` loop terminates, it means either `j` has become negative (meaning `key` is the smallest element so far) or `key` is no longer smaller than `arr[j]` (meaning `arr[j]` is in its correct position relative to `key`). The correct position for `key` is `j + 1`.
    *   `key` is inserted at `arr[j + 1]`.

5.  **Return:** After the outer `for` loop completes, the entire list `arr` is sorted in-place. The function returns the modified `arr`.

## Complexity Analysis

*   **Time Complexity:**
    *   **Best Case:** O(n) - This occurs when the input array is already sorted. The inner `while` loop will execute at most once for each element, performing a constant number of operations.
    *   **Average Case:** O(n^2) - This occurs when the input array is in a random order.
    *   **Worst Case:** O(n^2) - This occurs when the input array is sorted in reverse order. For each element, it needs to be compared with all preceding elements and shifted.

*   **Space Complexity:**
    *   **O(1)** - Insertion Sort is an in-place sorting algorithm. It only requires a constant amount of extra space for variables like `key` and `j`, regardless of the input size.