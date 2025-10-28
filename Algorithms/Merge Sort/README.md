# Merge Sort

## Introduction
Merge Sort is a classic comparison-based, divide-and-conquer sorting algorithm. It works by recursively dividing the input list into two halves until each sublist contains a single element, then merging those sublists back together in sorted order. Merge Sort is efficient and stable, with a consistent time complexity of O(n log n), making it suitable for sorting large datasets where guaranteed performance is critical.

## When to Use Merge Sort
- When you require stable sorting (preserves the relative order of equal elements).
- When you want predictable O(n log n) performance.
- When working with linked lists or external storage where sequential data access is more practical.
- When you want a sorting algorithm that does not rely on random access (though this Python implementation uses lists which support this).

## Usage
Example usage of the merge_sort function:
unsorted_list = [34, 7, 23, 32, 5, 62]
sorted_list = merge_sort(unsorted_list)
print(sorted_list)  # Output: [5, 7, 23, 32, 34, 62]

# The original list remains unchanged:
print(unsorted_list)  # Output: [34, 7, 23, 32, 5, 62]

## Detailed Explanation
1. **Base Case:** The recursion stops when the list is empty or contains only one element, as such lists are inherently sorted.

2. **Divide:** The list is split into two roughly equal halves using slicing.

3. **Conquer:** The function recursively sorts both halves.

4. **Merge:** Two sorted sublists are merged into a single sorted list by comparing the elements at the front of each sublist and appending the smaller to the result, advancing the pointer in the list from which the element was taken.

5. **Purity:** The function does not mutate the input list; instead, it returns a new sorted list, ensuring a pure function with no side effects.

## Complexity Analysis
- **Time Complexity:** O(n log n) in all cases (best, average, worst) due to the divide-and-conquer approach.
- **Space Complexity:** O(n) additional space due to the auxiliary lists created for merging.
- The algorithm requires extra space proportional to the input size since it cannot sort in place in this implementation.

This implementation is straightforward and clean, making it easy to understand, reuse, and integrate into other Python projects requiring a reliable sorting method.