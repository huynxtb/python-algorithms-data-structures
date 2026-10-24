## Selection Sort

### 1. Introduction
Selection Sort is a simple, in-place comparison sorting algorithm. It works by repeatedly finding the minimum element (or maximum, depending on the sort order) from the unsorted portion of the list and moving it to the sorted portion. It's generally not efficient for large lists due to its quadratic time complexity, but it's easy to understand and implement, making it useful for educational purposes or very small datasets where simplicity and minimal auxiliary space are prioritized.

### 2. Usage
To use the `selection_sort` function, simply pass a mutable list of comparable elements to it. The list will be sorted in-place.


my_list = [64, 25, 12, 22, 11]
selection_sort(my_list)
print(my_list) # Output: [11, 12, 22, 25, 64]

another_list = [5, 1, 4, 2, 8]
selection_sort(another_list)
print(another_list) # Output: [1, 2, 4, 5, 8]

string_list = ["banana", "apple", "cherry", "date"]
selection_sort(string_list)
print(string_list) # Output: ['apple', 'banana', 'cherry', 'date']


### 3. Detailed Explanation
The `selection_sort` function takes a mutable list `arr` as input and sorts it in ascending order directly within the provided list (in-place).

1.  **Outer Loop (`for i in range(n)`):** This loop iterates from the first element to the second-to-last element of the list. The variable `i` marks the boundary between the sorted part (elements from `0` to `i-1`) and the unsorted part (elements from `i` to `n-1`). In each iteration, the goal is to place the correct minimum element into the `i`-th position.

2.  **Finding the Minimum (`min_idx = i`, `for j in range(i + 1, n)`):** Inside the outer loop, `min_idx` is initialized to `i`. This assumes the element at the current `i`-th position is the minimum in the unsorted subarray. The inner loop then iterates through the rest of the unsorted part of the list (from `i+1` to `n-1`). If an element `arr[j]` is found to be smaller than `arr[min_idx]`, `min_idx` is updated to `j`. After the inner loop completes, `min_idx` will hold the index of the smallest element in the unsorted subarray `arr[i...n-1]`.

3.  **Swapping (`if min_idx != i: arr[i], arr[min_idx] = arr[min_idx], arr[i]`):** After finding the true minimum element's index (`min_idx`) in the unsorted portion, we swap it with the element at the current `i`-th position. This effectively moves the smallest element of the unsorted part to its correct sorted position. The `if min_idx != i` check is an optimization to avoid unnecessary swaps if the element is already in its correct place.

This process continues until the outer loop finishes, at which point the entire list will be sorted.

### 4. Complexity Analysis

*   **Time Complexity:**
    *   **Worst Case:** O(n^2)
    *   **Average Case:** O(n^2)
    *   **Best Case:** O(n^2)
    Selection Sort performs approximately `n` comparisons in the first pass, `n-1` in the second, and so on. This results in `(n-1) + (n-2) + ... + 1 = n(n-1)/2` comparisons, which is quadratic, O(n^2). The number of swaps is at most `n-1`. Regardless of the initial order of elements, the algorithm always performs the same number of comparisons, leading to O(n^2) complexity in all cases.

*   **Space Complexity:**
    *   **O(1)**
    Selection Sort is an in-place sorting algorithm. It only requires a constant amount of extra space for a few variables (like `i`, `j`, `min_idx`, and a temporary variable for swapping), regardless of the input list size.