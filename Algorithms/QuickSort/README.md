# QuickSort Algorithm

## Introduction
QuickSort is a highly efficient, comparison-based sorting algorithm that follows the divide-and-conquer paradigm. It is widely used due to its average and practical performance being very good in most cases. QuickSort works by selecting a 'pivot' element from the array and partitioning other elements into two sub-arrays according to whether they are less than or greater than the pivot. These sub-arrays are then sorted recursively. The process continues until the base case of an empty or single-element array is reached, which is inherently sorted.

QuickSort is an in-place sort (does not require additional storage) and typically faster than other O(n^2) algorithms like Bubble Sort or Insertion Sort, especially on large datasets.

Use QuickSort when you need an efficient, general-purpose sorting algorithm with good average-case performance.

## Usage
Example usage of quick_sort:

arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr)
print(arr)  # Output will be [1, 5, 7, 8, 9, 10]

This code sorts the list in place; the original list is modified.

## Detailed Explanation
The provided implementation uses the Lomuto partition scheme:

- The last element in the current sub-array is chosen as the pivot.
- During the partition phase, all elements smaller than or equal to the pivot are moved to the left side of the pivot.
- We keep track of the position where we'll swap smaller elements to ensure correct partitioning.
- After looping through the array, the pivot is swapped into its final position.

The `quick_sort_recursive` function is called initially for the whole array and recursively calls itself for the portions before and after the pivot’s position until the base condition (a sub-array of size 0 or 1) is reached.

This recursive approach ensures the entire list is sorted efficiently.

## Complexity Analysis
- **Time Complexity:**
  - Average Case: O(n log n), where n is the number of elements. The array is split approximately in half every recursion level.
  - Worst Case: O(n^2), occurs when the smallest or largest element is always chosen as the pivot (e.g., sorted or reverse-sorted input).

- **Space Complexity:** O(log n) due to recursion stack space in the average case; O(n) in the worst case if recursion depth grows linearly.

This implementation does not require additional arrays, sorting the list in-place.

---

Use this QuickSort implementation for educational purposes or anytime a simple, elegant, in-place sorting is required.