# Bubble Sort

## 1. Introduction
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. The algorithm gets its name because smaller or larger elements "bubble" to the top or bottom of the list, respectively, with each pass.

While easy to understand and implement, Bubble Sort is generally inefficient for large lists compared to more advanced sorting algorithms like Merge Sort or Quick Sort. It is primarily used for educational purposes or for very small datasets.

## 2. Usage
To use the `bubble_sort` function, simply pass a list of comparable elements to it. The function will sort the list in-place.


# Assuming the bubble_sort function is defined as above

# Example with integers
my_list = [64, 34, 25, 12, 22, 11, 90]
print(f"Original list: {my_list}")
bubble_sort(my_list)
print(f"Sorted list: {my_list}")
# Expected output:
# Original list: [64, 34, 25, 12, 22, 11, 90]
# Sorted list: [11, 12, 22, 25, 34, 64, 90]

# Example with strings
my_string_list = ["banana", "apple", "cherry", "date"]
print(f"Original string list: {my_string_list}")
bubble_sort(my_string_list)
print(f"Sorted string list: {my_string_list}")
# Expected output:
# Original string list: ['banana', 'apple', 'cherry', 'date']
# Sorted string list: ['apple', 'banana', 'cherry', 'date']


## 3. Detailed Explanation
The `bubble_sort` function works as follows:

1.  **Outer Loop (`for i in range(n - 1)`):** This loop controls the number of passes through the list. In each pass, at least one element is placed in its correct sorted position at the end of the unsorted portion of the list. After `i` passes, the last `i` elements are guaranteed to be in their final sorted positions. Therefore, we only need `n-1` passes in the worst case.

2.  **Inner Loop (`for j in range(n - 1 - i)`):** This loop iterates through the unsorted portion of the list. In each iteration, it compares `arr[j]` with `arr[j + 1]`. If `arr[j]` is greater than `arr[j + 1]`, it means they are in the wrong order, so they are swapped.
    *   The `n - 1 - i` range is crucial: `n - 1` ensures we don't go out of bounds when accessing `arr[j + 1]`. Subtracting `i` means we don't re-check elements that have already been placed in their correct sorted positions at the end of the list by previous passes.

3.  **`swapped` Flag Optimization:** A boolean variable `swapped` is introduced. It is set to `True` if any swaps occur during an inner loop pass. If an entire pass completes without any swaps (`swapped` remains `False`), it means the list is already sorted, and there's no need for further passes. This optimization allows the algorithm to terminate early in the best-case scenario (an already sorted list).

By repeatedly comparing and swapping adjacent elements, the largest unsorted element "bubbles up" to its correct position at the end of the unsorted portion of the list in each pass.

## 4. Complexity Analysis

*   **Time Complexity:**
    *   **Worst Case: O(n^2)** - This occurs when the list is sorted in reverse order. In this scenario, the algorithm performs `n-1` passes, and in each pass, the inner loop runs approximately `n` times, leading to `(n-1) * (n-1)` comparisons and swaps.
    *   **Average Case: O(n^2)** - For a randomly ordered list, the number of comparisons and swaps remains proportional to `n^2`.
    *   **Best Case: O(n)** - This occurs when the list is already sorted. The `swapped` flag optimization ensures that the algorithm makes only one pass through the list (performing `n-1` comparisons) and then terminates, as no swaps will occur.

*   **Space Complexity:**
    *   **O(1)** - Bubble Sort is an in-place sorting algorithm. It only requires a constant amount of extra space for a few variables (like `n`, `i`, `j`, and `swapped`), regardless of the input list size.